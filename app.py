from flask import Flask, render_template, request
from extractor import extract_text_from_pdf, parse_sbi_statement, parse_axis_statement
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    bank_type = request.form.get('bank')

    if not file or not file.filename.endswith('.pdf'):
        return "Invalid file."

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    text = extract_text_from_pdf(file_path)

    if bank_type == "sbi":
        data = parse_sbi_statement(text)
    elif bank_type == "axis":
        data = parse_axis_statement(text)
    else:
        data = {"error": "Bank not supported."}

    return render_template("result.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)