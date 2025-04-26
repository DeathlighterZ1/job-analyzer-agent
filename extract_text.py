import PyPDF2
import docx
import requests

def extract_text_from_file(uploaded_file):
    if uploaded_file.name.endswith('.pdf'):
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

    elif uploaded_file.name.endswith('.docx'):
        doc = docx.Document(uploaded_file)
        return "\n".join([para.text for para in doc.paragraphs])

    elif uploaded_file.name.endswith(('.jpg', '.jpeg', '.png')):
        api_key = "K83923773588957"
        url = "https://api.ocr.space/parse/image"
        response = requests.post(url,
                                 files={"file": uploaded_file},
                                 data={"apikey": api_key})
        result = response.json()
        return result["ParsedResults"][0]["ParsedText"]
