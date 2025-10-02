import os
import shutil
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama.llms import OllamaLLM
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

app = Flask(__name__)

# --- 기본 설정 ---
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf'}

# --- 모델 및 경로 설정 ---
model_name = "exaone3.5:2.4b"
embedding_model_name = "jhgan/ko-sroberta-multitask"
vector_store_path = "faiss_index"

# --- 전역 변수 ---
# RAG 체인을 저장할 변수 (메모리 포함)
qa_chain = None

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def setup_rag_pipeline(file_path):
    """
    특정 파일 경로를 기반으로 RAG 파이프라인을 설정하고 생성합니다.
    """
    global qa_chain

    # 기존 벡터 저장소 삭제
    if os.path.exists(vector_store_path):
        shutil.rmtree(vector_store_path)
        print(f"기존 '{vector_store_path}'를 삭제했습니다.")

    # 1. 파일 확장자에 따라 적절한 로더 선택
    if file_path.lower().endswith('.pdf'):
        loader = PyPDFLoader(file_path)
        documents = loader.load()
    elif file_path.lower().endswith('.txt'):
        try:
            # 1. UTF-8으로 먼저 시도
            print(file_path)
            loader = TextLoader(file_path, encoding='utf-8')
            documents = loader.load()
        except Exception as e:
            print(f"UTF-8 로딩 실패: {e}. cp949로 재시도합니다.")
            try:
                # 2. cp949로 재시도
                loader = TextLoader(file_path, encoding='cp949')
                documents = loader.load()
            except Exception as e2:
                print(f"cp949 로딩 실패: {e2}. euc-kr로 재시도합니다.")
                try:
                    # 3. euc-kr로 재시도
                    loader = TextLoader(file_path, encoding='euc-kr')
                    documents = loader.load()
                except Exception as e3:
                    # 모든 인코딩 실패 시 오류 발생
                    raise IOError(f"{os.path.basename(file_path)} 파일을 utf-8, cp949, euc-kr 인코딩으로 읽는 데 모두 실패했습니다.") from e3
    else:
        raise ValueError("지원하지 않는 파일 형식입니다.")
    print(f"'{os.path.basename(file_path)}' 문서를 로드했습니다.")

    # 2. 텍스트 분할
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_documents(documents)
    print(f"문서를 {len(texts)}개의 조각으로 분할했습니다.")

    # 3. 임베딩 및 벡터 저장소 생성
    embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)
    vector_store = FAISS.from_documents(texts, embeddings)
    vector_store.save_local(vector_store_path)
    print(f"'{vector_store_path}'에 새로운 벡터 저장소를 생성하고 저장했습니다.")

    # 4. LLM 및 대화 메모리 설정
    llm = OllamaLLM(model=model_name)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # 5. 대화형 RAG 체인 생성
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory
    )
    print("새로운 문서를 기반으로 RAG 파이프라인이 성공적으로 설정되었습니다.")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        print(f"파일 저장 완료: {file_path}")

        try:
            # 파일 업로드 후 RAG 파이프라인 설정
            setup_rag_pipeline(file_path)
            return jsonify({"message": "File processed successfully", "filename": filename})
        except Exception as e:
            print(f"파이프라인 설정 오류: {e}")
            return jsonify({"error": f"Failed to process file: {e}"}), 500

    return jsonify({"error": "File type not allowed"}), 400

@app.route("/ask", methods=["POST"])
def ask_route():
    global qa_chain
    if not qa_chain:
        return jsonify({"error": "Pipeline not initialized. Please upload a file first."}), 400

    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        result = qa_chain.invoke({"question": user_message})
        ai_response = result.get("answer", "답변을 생성하지 못했습니다.")
        return jsonify({"response": ai_response})
    except Exception as e:
        print(f"챗봇 답변 오류: {e}")
        return jsonify({"error": f"Error during conversation: {e}"}), 500

if __name__ == "__main__":
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    # 앱 시작 시에는 파이프라인을 설정하지 않고, 파일 업로드 시 설정하도록 변경
    app.run(debug=True, host='0.0.0.0', port=5000)
