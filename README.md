Keyword Extractor
This project is a Keyword Extraction System designed to extract important keywords from uploaded documents (PDF, DOC, PPT) or directly pasted text. The system uses the RAKE (Rapid Automatic Keyword Extraction) algorithm to provide users with the key topics and phrases from their content.

Features
Document Upload: Supports keyword extraction from PDF, DOC, and PPT files.
Direct Text Input: Users can paste their text directly into the interface for extraction.
Keyword Extraction: Powered by the RAKE algorithm for fast and relevant keyword generation.
Single View: Simple interface where users upload a document or paste text, and the extracted keywords are displayed on the same page.
Tech Stack
Backend: Flask (Python), integrated with the RAKE model for keyword extraction.
Frontend: HTML, CSS for a clean user interface.
RAKE Algorithm: Used for efficient keyword extraction.
Installation
To set up the project locally, follow these steps:

Prerequisites
Python 3.x
Flask
RAKE
Steps
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/keyword-extractor.git
cd keyword-extractor
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
python app.py
Open your browser and visit:

arduino
Copy code
http://127.0.0.1:5000/
Usage
Upload a Document/Enter Text: Either upload a file (PDF, DOC, PPT) or paste your text into the input box.
View Keywords: The system will display extracted keywords on the same page after processing.
Directory Structure
php
Copy code
.
├── app.py                # Main application file
├── static/               # Static files (CSS, images)
├── templates/            # HTML templates (single view for document input)
├── models/               # RAKE model integration
├── uploads/              # Folder for storing user uploads
├── README.md             # This file
└── requirements.txt      # Project dependencies
License
This project is licensed under the MIT License - see the LICENSE file for details.
