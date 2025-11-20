
import os
import gradio as gr
from huggingface_hub import InferenceClient

# Correct model ID & API client
client = InferenceClient(
    model="meta-llama/Llama-3.1-8B-Instruct",
    token=os.environ["HF_TOKEN"]
)

# Load Act text
with open("full_text.txt", "r", encoding="utf-8") as f:
    ACT_TEXT = f.read()

def answer_question(question):
    messages = [
        {"role": "system", "content": "You are a legal assistant. Answer ONLY using the Act text. If not found, say: 'The Act does not provide this information.'"},
        {"role": "user", "content": f"Act Text:\n{ACT_TEXT}\n\nQuestion: {question}"}
    ]

    response = client.chat_completion(
        messages=messages,
        max_tokens=300,
    )

    return response.choices[0].message["content"]

# UI
with gr.Blocks() as demo:
    gr.Markdown("# 📘 Universal Credit Act Q&A Assistant")
    question = gr.Textbox(label="Ask a Question")
    answer = gr.Textbox(label="Answer", lines=10)
    btn = gr.Button("Get Answer")
    btn.click(answer_question, inputs=question, outputs=answer)
demo.launch()

