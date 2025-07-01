# 🧾 PDF Credit Card Statement Parser

A personal web-based software to upload **bank credit card PDF statements**, extract key financial information like **Total Bill Amount**, automatically **categorize expenses**, and **append them to an Excel sheet** — designed for personal use, later open-sourcing planned.

---

## 🔧 Features

- 📤 Upload credit card statements (PDF format)
- 📄 Extract raw text from PDFs using PyMuPDF
- 💡 Detect total bill amount (in progress)
- 🧠 Auto-categorize spending based on descriptions (planned)
- 📊 Append results to an Excel report for tracking
- ⚙️ Built with Python and Flask

---

## 🗂️ Project Structure

credit_parser/
├── app.py # Main Flask app
├── extractor.py # PDF text extraction logic
├── templates/
│ └── index.html # Upload form and display
├── uploads/ # Folder to save uploaded PDFs
├── env/ # Virtual environment (not uploaded to Git)
└── README.md # This file



---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/credit-parser.git
cd credit-parser
```
2. Setup virtual environment

```
python -m venv env
env\Scripts\activate  # On Windows
```

3. Install dependencies

```
pip install flask pymupdf python-dotenv
```

4. Run the server

```
python app.py
```

Visit http://127.0.0.1:5000 in your browser.

<br>

## 💡 Why This Project?
- Managing and understanding credit card bills manually is error-prone. This tool helps automate:

- Tracking real spending patterns

- Detecting unnecessary charges

- Creating reports without Excel formulas

## ⚠️ Disclaimer
This is a personal project under development and not production-grade software. Always verify results before relying on them.

## 📚 License
This project will be open-sourced in the future under the MIT License.

Developed by [Sayan Mondal](https://linkedin.com/analystsayan).