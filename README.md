# 📄 Keyword Extractor

A simple web-based **Keyword Extraction System** that allows users to extract important keywords from documents or text using the **RAKE (Rapid Automatic Keyword Extraction)** algorithm. This tool is designed to quickly provide the key topics and phrases from your content.

---

## ✨ Features

- **Upload Documents**: Extract keywords from PDF, DOC, or PPT files.
- **Paste Text**: Directly paste your text to extract keywords.
- **RAKE Algorithm**: Automatically identifies key phrases efficiently.

The interface is simple, with just one view where users can upload documents or input text, and the extracted keywords are displayed on the same page.

---

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS
- **Keyword Extraction**: RAKE algorithm

---

## 🚀 Installation

Follow the steps below to set up the project locally:

### Prerequisites

Ensure you have the following installed:
- Python 3.x
- Flask
- RAKE

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/keyword-extractor.git
    cd keyword-extractor
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask application**:
    ```bash
    python app.py
    ```

5. **Access the application**:  
   Open your browser and navigate to:  
