# 📝 Markdown File Viewer & Converter Web App

A simple yet powerful **Streamlit** web application that allows you to:

✅ Upload `.md` (Markdown) files  
✅ Preview them in a styled pop-up  
✅ Convert to **PDF**, **HTML**, or **Plain Text**  
✅ Download the converted file instantly  

---

## 🚀 Features

- 📤 Upload any `.md` file
- 👀 View content in a clean, scrollable preview
- 🔄 Convert to:
  - PDF (via `pdfkit`)
  - HTML (via `markdown2`)
  - Plain Text
- 📥 Download button for your chosen format
- ⚙️ Easy to use & portable

---

## 📸 Screenshot

<img width="1916" height="946" alt="image" src="https://github.com/user-attachments/assets/0ffa07c6-0950-456d-8369-b84dcd88b7b0" />


---

## 🧰 Tech Stack

- [Python 3.8+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [pdfkit](https://pypi.org/project/pdfkit/)
- [markdown2](https://pypi.org/project/markdown2/)
- [wkhtmltopdf](https://wkhtmltopdf.org/) (used internally for PDF conversion)

---

## 📦 Installation

Clone this repo and set up a virtual environment:

```bash
git clone https://github.com/Theubaa/.md-to-pdf-html-text-converter.git
cd .md-to-pdf-html-text-converter
python -m venv venv
venv\Scripts\activate   # On Windows
pip install -r requirements.txt
🛠️ Also install wkhtmltopdf manually (1-time setup):
PDF generation uses pdfkit, which relies on wkhtmltopdf under the hood.

Step 1: Download & Install
🔗 Download wkhtmltopdf
Choose the version that matches your OS.

Step 2: Add to Environment Variables
After installation, add the following path to your PATH variable:

makefile

C:\Program Files\wkhtmltopdf\bin
Restart your terminal or system if needed.

▶️ Run the App
bash

streamlit run app.py
The app will open in your browser automatically.

🧪 Sample Files
Drop your .md files into the uploader to try the preview and export features.

🙌 Contributing
Feel free to fork this repo, suggest improvements or request features via issues.

📄 License
MIT License © 2025 Theubaa
