import gradio as gr
from rag_pipeline import process_pdf, ask_question_with_rag
import os, time

def handle_upload(pdf_file):
    os.makedirs("data", exist_ok=True)
    filename = f"upload_{int(time.time())}.pdf"
    path = os.path.join("data", filename)

    with open(path, "wb") as f:
        f.write(pdf_file)
        

    process_pdf(path)
    return f"✅ {filename} 업로드 완료", True

def handle_query(query, uploaded):
    if not uploaded:
        return "⚠️ 먼저 PDF를 업로드해 주세요!"
    return ask_question_with_rag(query)

with gr.Blocks() as demo:
    gr.Markdown("## 📄 PDF 기반 Q&A 챗봇")
    uploaded_state = gr.State(False)

    with gr.Row():
        pdf_input = gr.File(label="PDF 업로드", file_types=[".pdf"], type="binary")  # ✅ 여기!
        upload_btn = gr.Button("업로드 및 분석")
        upload_status = gr.Textbox(label="업로드 상태")

    with gr.Row():
        question_input = gr.Textbox(label="질문 입력")
        ask_btn = gr.Button("질문하기")
        answer_output = gr.Textbox(label="GPT 답변")

    upload_btn.click(fn=handle_upload, inputs=[pdf_input], outputs=[upload_status, uploaded_state])
    ask_btn.click(fn=handle_query, inputs=[question_input, uploaded_state], outputs=[answer_output])

demo.launch()
