# ai-pdf-rag-chatbot

# 📄 AI PDF 기반 Q&A 챗봇 (LangChain + Gradio)

이 프로젝트는 업로드한 PDF 문서를 기반으로 질문을 하면, GPT가 관련 내용을 검색하고 답변을 생성해주는 **RAG (Retrieval-Augmented Generation)** 챗봇입니다. 
LangChain, FAISS, OpenAI, Gradio를 활용해 빠르게 웹 기반 챗봇을 구축할 수 있습니다.

---

## 🚀 기능 요약

- ✅ PDF 업로드 → 자동 청크 분할
- ✅ OpenAI 임베딩 모델로 벡터화
- ✅ FAISS를 이용한 벡터 저장 및 검색
- ✅ GPT-4o-mini를 통한 자연어 질문 응답
- ✅ Gradio UI 웹앱 제공

---

## 📂 폴더 구조

```
ai-pdf-rag-chatbot/
├── app.py                    # Gradio 웹 인터페이스
├── rag_pipeline.py          # PDF 처리 및 RAG 응답 처리
├── api_key.txt              # OpenAI API 키 (로컬 사용용)
├── requirements.txt         # 의존성 목록
├── data/                    # 업로드된 PDF 저장소
├── vectordb/                # FAISS 벡터 저장소 (자동 생성)
└── README.md
```

---

## ⚙️ 실행 방법

### 1. 프로젝트 클론 및 진입
```bash
git clone https://github.com/your-id/ai-pdf-rag-chatbot.git
cd ai-pdf-rag-chatbot
```

### 2. 가상환경 설치 및 패키지 설치
```bash
python -m venv venv
source venv/bin/activate  # 윈도우는 venv\Scripts\activate
pip install -r requirements.txt
```

### 3. OpenAI API 키 설정
`api_key.txt` 파일 생성 후 아래와 같이 작성:
```
OPENAI_API_KEY=sk-xxxxx...
```

### 4. 앱 실행
```bash
python app.py
```
웹 브라우저에서 자동으로 http://127.0.0.1:7860 열림

---

## 💡 사용 예시

1. PDF 업로드 (예: 인공지능 윤리 가이드북)
2. 질문: `"이 문서에서 가장 중요한 내용은?"`
3. 응답: GPT가 벡터DB에서 관련 문서 검색 후 요약 생성

---

## 📚 사용 기술

- [LangChain](https://www.langchain.com/)
- [OpenAI GPT-4o](https://platform.openai.com/docs)
- [FAISS](https://github.com/facebookresearch/faiss)
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)
- [Gradio](https://www.gradio.app/)

---

## 🧠 확장 아이디어

- ✅ Chroma로 DB 전환
- ✅ Streamlit UI로 리팩토링
- ✅ 문서 요약 자동 출력 기능
- ✅ 질문에 따라 하이라이팅 표시
- ✅ 다양한 문서 포맷 (txt, csv 등) 지원

---

## 📄 License

MIT License
# 📄 AI PDF 기반 Q&A 챗봇 (LangChain + Gradio)

이 프로젝트는 업로드한 PDF 문서를 기반으로 질문을 하면, GPT가 관련 내용을 검색하고 답변을 생성해주는 **RAG (Retrieval-Augmented Generation)** 챗봇입니다. 
LangChain, FAISS, OpenAI, Gradio를 활용해 빠르게 웹 기반 챗봇을 구축할 수 있습니다.

---

## 🚀 기능 요약

- ✅ PDF 업로드 → 자동 청크 분할
- ✅ OpenAI 임베딩 모델로 벡터화
- ✅ FAISS를 이용한 벡터 저장 및 검색
- ✅ GPT-4o-mini를 통한 자연어 질문 응답
- ✅ Gradio UI 웹앱 제공

---

## 📂 폴더 구조

```
ai-pdf-rag-chatbot/
├── app.py                    # Gradio 웹 인터페이스
├── rag_pipeline.py          # PDF 처리 및 RAG 응답 처리
├── api_key.txt              # OpenAI API 키 (로컬 사용용)
├── requirements.txt         # 의존성 목록
├── data/                    # 업로드된 PDF 저장소
├── vectordb/                # FAISS 벡터 저장소 (자동 생성)
└── README.md
```

---

## ⚙️ 실행 방법

### 1. 프로젝트 클론 및 진입
```bash
git clone https://github.com/your-id/ai-pdf-rag-chatbot.git
cd ai-pdf-rag-chatbot
```

### 2. 가상환경 설치 및 패키지 설치
```bash
python -m venv venv
source venv/bin/activate  # 윈도우는 venv\Scripts\activate
pip install -r requirements.txt
```

### 3. OpenAI API 키 설정
`api_key.txt` 파일 생성 후 아래와 같이 작성:
```
OPENAI_API_KEY=sk-xxxxx...
```

### 4. 앱 실행
```bash
python app.py
```
웹 브라우저에서 자동으로 http://127.0.0.1:7860 열림

---

## 💡 사용 예시

1. PDF 업로드 (예: 인공지능 윤리 가이드북)
2. 질문: `"이 문서에서 가장 중요한 내용은?"`
3. 응답: GPT가 벡터DB에서 관련 문서 검색 후 요약 생성

---

## 📚 사용 기술

- [LangChain](https://www.langchain.com/)
- [OpenAI GPT-4o](https://platform.openai.com/docs)
- [FAISS](https://github.com/facebookresearch/faiss)
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)
- [Gradio](https://www.gradio.app/)

---

## 🧠 확장 아이디어

- ✅ Chroma로 DB 전환
- ✅ Streamlit UI로 리팩토링
- ✅ 문서 요약 자동 출력 기능
- ✅ 질문에 따라 하이라이팅 표시
- ✅ 다양한 문서 포맷 (txt, csv 등) 지원

---

## 📄 License

MIT License

## 실행 결과

![image](https://github.com/user-attachments/assets/a6a1ca07-f6a4-4d93-89e7-a458ceb188a1)
