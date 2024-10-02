# import google.generativeai as genai

# genai.configure(api_key="AIzaSyC7Hc7qO-4nea72gpzaNqmblkBsbNI7fRQ")
# print("Google AI configured.")

# from IPython.display import display
# from IPython.display import Markdown
# import textwrap
# import warnings
# from pathlib import Path as p
# from pprint import pprint
# import pandas as pd
# from langchain import PromptTemplate
# from langchain.chains.question_answering import load_qa_chain
# from langchain.document_loaders import PyPDFLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.vectorstores import FAISS  # Changed to FAISS
# from langchain.chains import RetrievalQA
# from langchain.document_loaders import PyPDFDirectoryLoader
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain_google_genai import ChatGoogleGenerativeAI

# warnings.filterwarnings("ignore")

# # Load PDF documents from directory
# pdf_directory_loader = PyPDFDirectoryLoader("pdfs")
# documents = pdf_directory_loader.load()
# print(f"Loaded {len(documents)} documents.")

# # Limit the number of documents for testing (e.g., first 5 documents)
# limited_documents = documents[:5]  # Adjust this number based on your needs

# # Split text into chunks
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=500)
# context = "\n\n".join(str(p.page_content) for p in limited_documents)
# texts = text_splitter.split_text(context)
# print(f"Created {len(texts)} text chunks.")

# # Create embeddings
# embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key="AIzaSyC7Hc7qO-4nea72gpzaNqmblkBsbNI7fRQ")
# print("Embeddings created successfully.")

# # Create vector index using FAISS
# faiss_vector_index = FAISS.from_texts(texts, embeddings)
# print("FAISS vector index created successfully.")

# # Initialize Chat model
# model = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key="AIzaSyC7Hc7qO-4nea72gpzaNqmblkBsbNI7fRQ",
#                              temperature=0.2, convert_system_message_to_human=True)

# # Set up the QA chain
# template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer.
# {context}
# Question: {question}
# Helpful Answer:"""
# QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

# qa_chain = RetrievalQA.from_chain_type(
#     model,
#     retriever=faiss_vector_index.as_retriever(),  # Use FAISS retriever
#     return_source_documents=True,
#     chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
# )

# # Run the QA chain with a sample question
# question = "What is Sound"
# result = qa_chain({"query": question})
# print(result["result"])

import requests

url = "https://api.sarvam.ai/text-to-speech"

payload = {
    "inputs": ["\"The answer lies in the format below\""],
    "target_language_code": "en-IN",
    "speaker": "meera",
    "pitch": .5
}
headers = {
    "api-subscription-key": "101e1efb-e49a-46b6-b886-f8e32c0e5ec0",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

res = response.json()
audio = res.get("audios")
# save it as .wav file after base64 decoding
import base64
audio_bytes = base64.b64decode(audio[0])
with open("response.wav", "wb") as f:
    f.write(audio_bytes)
print("done")