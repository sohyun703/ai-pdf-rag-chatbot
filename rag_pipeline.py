from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationalRetrievalChain
import os


# API 키 로딩
def load_api_keys(filepath="api_key.txt"):
    with open(filepath, "r") as f:
        for line in f:
            if "=" in line:
                key, value = line.strip().split("=", 1)
                os.environ[key] = value

load_api_keys()

# PDF 처리 + 벡터 DB 저장
def process_pdf(file_path):
    loader = PyMuPDFLoader(file_path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    split_docs = splitter.split_documents(docs)
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vectordb = FAISS.from_documents(split_docs, embeddings)
    vectordb.save_local("vectordb")
    return vectordb

# 질문 처리
def ask_question_with_rag(query):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vectordb = FAISS.load_local("vectordb", embeddings, allow_dangerous_deserialization=True)
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.3)

    memory = ConversationSummaryMemory(llm=llm, memory_key="chat_history", return_messages=True, output_key="answer")

    prompt = ChatPromptTemplate.from_messages([
        ("system", "너는 업로드된 PDF 문서의 전문가야. 질문에 간결하고 정확하게 답해줘."),
        ("human", "질문: {question}\n\n관련 문서:\n{context}")
    ])

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        output_key="answer",
        return_source_documents=True,
        combine_docs_chain_kwargs={"prompt": prompt}
    )

    result = qa_chain({"question": query})
    return result["answer"]
