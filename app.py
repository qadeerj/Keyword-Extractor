from flask import Flask, render_template, request, redirect, url_for
import os
import pickle
from werkzeug.utils import secure_filename
import pdfplumber
import docx

# Initialize Flask app
app = Flask(__name__)

# Folder for uploaded files
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt'}

# Load the KeyBERT model
with open('keybert_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Check if file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Extract text from .docx file
def read_docx(file_path):
    doc = docx.Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

# Extract text from PDF file using pdfplumber
def read_pdf(file_path):
    text = ''
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ''  # Extract text from each page
    return text

# Extract text from .txt file
def read_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

# Route for homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the file part is present in the request
    if 'file' not in request.files:
        return "No file part in the request", 400  # Error if file part is missing

    file = request.files['file']

    # Check if file is selected
    if file.filename == '':
        return "No file selected", 400  # Error if no file is selected

    # Check if the file is valid and has allowed extension
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Extract text from the uploaded document based on file type
        if filename.endswith('.txt'):
            content = read_txt(file_path)
        elif filename.endswith('.pdf'):
            content = read_pdf(file_path)  # Use the updated read_pdf function
        elif filename.endswith('.docx'):
            content = read_docx(file_path)
        else:
            return "Unsupported file type", 400

        # Extract keywords using KeyBERT model
        keywords = model.extract_keywords(content, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=5)

        # Render the keywords in the frontend
        return render_template('index.html', keywords=[kw[0] for kw in keywords])

    return "File type not allowed", 400  # Error if file type is not allowed

# Run the Flask app
if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
