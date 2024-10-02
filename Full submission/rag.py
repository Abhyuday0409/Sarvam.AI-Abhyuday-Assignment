import google.generativeai as genai
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS  # Changed to FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain import PromptTemplate

def configure_ai(api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="gemini-pro")
    return model

def load_documents():
    pdf_directory_loader = PyPDFDirectoryLoader("pdfs")
    documents = pdf_directory_loader.load()
    return documents

def prepare_vector_index(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=500)  # Adjusted chunk sizes
    context = "\n\n".join(str(doc.page_content) for doc in documents)
    texts = text_splitter.split_text(context)

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key="GOOGLE-API-KEY")
    vector_index = FAISS.from_texts(texts, embeddings)  # Use FAISS for the vector index
    return vector_index.as_retriever(search_kwargs={"k": 2})

def ask_question(question):
    documents = load_documents()
    vector_index = prepare_vector_index(documents)

    model = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key="AIzaSyC7Hc7qO-4nea72gpzaNqmblkBsbNI7fRQ", temperature=0.2, convert_system_message_to_human=True)

    template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer.
    {context}
    Question: {question}
    Helpful Answer:"""
    QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

    qa_chain = RetrievalQA.from_chain_type(
        model,
        retriever=vector_index,
        return_source_documents=True,
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
    )

    result = qa_chain({"query": question})
    answer = result["result"]
    source_documents = result["source_documents"]
    return answer, source_documents
