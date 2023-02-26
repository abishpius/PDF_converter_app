import streamlit as st
import PyPDF2

st.title("Free Pdf to Text Converter")
st.subheader("Converts a single pdf file to text file")

upload_file = st.file_uploader('Choose your .pdf file', type="pdf")

if upload_file is not None:
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfReader(upload_file)

    # printing number of pages in pdf file
    print(len(pdfReader.pages))

    # Create a string variable to store the text content
    text_content = ""

    # creating a page object
    for i in range(len(pdfReader.pages)):
        pageObj = pdfReader.pages[i]
        # extracting text from page
        text_content += pageObj.extract_text()

    
    # Open a TXT file and write the text content into it
    st.download_button('Download as text', text_content,file_name='pdf_converted.txt')