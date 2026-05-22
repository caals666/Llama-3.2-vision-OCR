# Llama-3.2-vision-OCR

Extract structured, readable text from images using **Llama 3.2 Vision** — running locally via Ollama.

---

## Features

- Upload PNG, JPG, or JPEG images
- Extracts all readable text using a local vision LLM
- Outputs clean, structured **Markdown** (headings, lists, code blocks, etc.)
- Simple one-click interface built with Streamlit

---

## Prerequisites

- Python 3.9+
- [Ollama](https://ollama.com) installed and running locally
- The `llama3.2-vision:11b` model pulled

---

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/your-username/llama-ocr.git
cd llama-ocr
```

**2. Install dependencies**
```bash
pip install streamlit ollama pillow
```

**3. Pull the vision model**
```bash
ollama pull llama3.2-vision:11b
```

**4. Run the app**
```bash
streamlit run app.py
```

---

## Usage

1. Open the app in your browser (typically `http://localhost:8501`)
2. Use the **sidebar** to upload an image
3. Click **"Extract Text"**
4. The extracted content appears in the main panel as formatted Markdown
5. Use **"Clear Image"** to reset and start over

---

## Project Structure

```
llama-ocr/
├── app.py        # Main Streamlit application
└── README.md
```

---

## Notes

- All processing happens **locally** — no data is sent to external APIs
- Accuracy depends on image quality and text clarity
- For best results, use high-resolution images with clearly legible text