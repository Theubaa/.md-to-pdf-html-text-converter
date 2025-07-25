import streamlit as st
import markdown
import pdfkit
import tempfile
import os

st.set_page_config(page_title="Markdown to PDF Converter", layout="centered")
st.title("📄 Markdown to PDF Converter")

# File upload
uploaded_file = st.file_uploader("Upload a Markdown (.md) file", type=["md"])

if uploaded_file is not None:
    # Read and display markdown content
    md_content = uploaded_file.read().decode("utf-8")
    st.subheader("📘 Markdown Preview")
    st.markdown(md_content, unsafe_allow_html=True)

    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content)

    # PDF Conversion & Download
    if st.button("📥 Convert to PDF"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_pdf:
            try:
                pdfkit.from_string(html_content, tmp_pdf.name)
                with open(tmp_pdf.name, "rb") as f:
                    st.download_button(
                        label="⬇️ Download PDF",
                        data=f,
                        file_name="converted.pdf",
                        mime="application/pdf"
                    )
            except OSError as e:
                st.error("❌ PDF conversion failed. Make sure wkhtmltopdf is installed and added to your system PATH.")
                st.code(str(e))

    # Optional: Convert to HTML download
    if st.button("🌐 Download as HTML"):
        st.download_button(
            label="⬇️ Download HTML",
            data=html_content,
            file_name="converted.html",
            mime="text/html"
        )
