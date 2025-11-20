# Universal Credit Act AI Agent

This repository contains an AI-powered legal assistant that analyzes the Universal Credit Act 2025, extracts structured information, evaluates rule compliance, and provides grounded question-answering. The project uses Llama 3.1 8B Instruct through HuggingFace Inference API and includes an optional Gradio-based deployment.

## Live Demo (HuggingFace Space)

**HuggingFace Space URL:** https://huggingface.co/spaces/alokik29/universal-credit-legal-agent

The deployed Space allows users to ask questions about the Act and receive answers strictly based on the legislative text.

---

## Project Overview

This project completes all required assignment components:

- Text extraction from PDF
- Chunking and cleaning
- Section extraction (definitions, obligations, responsibilities, eligibility, payments, penalties, record keeping)
- Conversion into structured JSON
- Rule validation with evidence and confidence
- Combined final JSON output
- Optional UI deployed on HuggingFace Spaces

All processing was implemented in Python via Google Colab.

---

## Repository Structure
```
universal-credit-act-ai-agent
│
├── credit_act_rag.ipynb      # Main Colab notebook with full assignment workflow
├── final_output.json          # Combined output of Task 3 and Task 4
├── full_text.txt              # Extracted text from the Act
├── app.py                     # Gradio-based Q&A application used for HF Space deployment
├── requirements.txt           # Dependencies for the deployment environment
└── README.md                  # Project documentation
```

---

## Assignment Breakdown

### Task 1: Text Extraction and Preprocessing

- Extracted full text from the Universal Credit Act 2025 PDF using a PDF parser.
- Cleaned formatting, removed extraneous line breaks, normalized spacing.
- Saved the full cleaned text into `full_text.txt`.

### Task 2: Section Extraction

Using an LLM, the Act was broken down into the following structured sections:

- `definitions`
- `obligations`
- `responsibilities`
- `eligibility`
- `payments`
- `penalties`
- `record_keeping`

Output was stored in memory for later processing.

### Task 3: JSON Structuring

The extracted sections were converted into a strict and consistent JSON schema. Final structured output is saved in `final_output.json`.

### Task 4: Rule Evaluation

Each rule was evaluated and classified as:

- `pass` or `fail`
- accompanied by evidence
- assigned a confidence score

The rule evaluation results are included alongside the extracted sections in `final_output.json`.

---

## Deployed Question-Answering System

The Gradio app (`app.py`) provides a simple interface that:

- Loads the full Act text automatically
- Accepts a user question
- Sends a grounded prompt to the Llama 3.1 8B Instruct model
- Returns an answer strictly based on the Act text
- Rejects hallucinations by providing a fallback message when the Act lacks the information

This app is deployed as a HuggingFace Space.

---

## Running Locally

### Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/universal-credit-act-ai-agent
cd universal-credit-act-ai-agent
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

### Run the notebook:
```bash
jupyter notebook credit_act_rag.ipynb
```

### To launch the Gradio app locally:
```bash
python app.py
```

---

## Technologies Used

- **Language Model:** Llama 3.1 8B Instruct (via HuggingFace Inference API)
- **Framework:** Gradio
- **Development Environment:** Google Colab
- **Deployment:** HuggingFace Spaces

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

This project was developed as part of an assignment to demonstrate AI-powered legal document analysis and question-answering capabilities.
