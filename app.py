import streamlit as st
from extract_text import extract_text_from_file
from analyze_text import analyze_cv_text

st.set_page_config(page_title="Job Analyzer Agent", layout="centered")

st.title("📄 Job Analyzer Agent")
st.write("Upload your CV and get a detailed feedback report!")

uploaded_file = st.file_uploader(
    "Upload your CV",
    type=["pdf", "docx", "jpg", "jpeg", "png"],
    help="Limit 200MB per file • PDF, DOCX, JPG, JPEG, PNG"
)

if uploaded_file:
    text = extract_text_from_file(uploaded_file)

    if text:
        feedback, score = analyze_cv_text(text)

        # Create full feedback report
        full_report = f"JOB ANALYZER REPORT\n---------------------\nScore: {score}/100\n\nDetailed Feedback:\n{feedback}"

        # Display the feedback report
        st.text_area("Feedback Report", full_report, height=400)

        # Download button
        st.download_button(
            label="📥 Download Report",
            data=full_report,
            file_name="cv_feedback_report.txt",
            mime="text/plain"
        )
    else:
        st.error("Failed to extract text from the uploaded file. Please try another file.")
