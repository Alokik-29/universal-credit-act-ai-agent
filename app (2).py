
import os
import gradio as gr
from huggingface_hub import InferenceClient

# Load model (token must be added in HF Space Settings → Variables)
client = InferenceClient(
    "meta-llama/Meta-Llama-3.1-8B-Instruct",
    token=os.environ.get("HF_TOKEN")
)

# ----------- Q&A Function -----------
def answer_question(question, act_text):
    prompt = f"""
You are a legal assistant trained to answer questions ONLY based on the Act text below.
If the answer is not present in the Act, say: 'The Act does not provide this information.'

Act Text:
{act_text}

Question: {question}

Answer:
"""

    response = client.text_generation(prompt, max_new_tokens=300)
    return response


# ----------- Gradio UI -----------
with gr.Blocks() as ui:
    gr.Markdown("# 📘 Universal Credit Act Q&A Assistant")
    gr.Markdown("Ask any question about the Act. The model will answer from the provided text.")

    question = gr.Textbox(label="Ask a Question", placeholder="e.g., What is a pre-2026 claimant?")
    act_text = gr.Textbox(label="Paste Act Text Here", lines=25)
    output = gr.Textbox(label="Answer")

    btn = gr.Button("Get Answer")
    btn.click(answer_question, inputs=[question, act_text], outputs=output)

ui.launch()
