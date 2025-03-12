import streamlit as st
import pandas as pd
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    return text.strip()

# Streamlit UI
st.title("📄 AI Resume Screening & Candidate Ranking System")

# Job Description Input
st.header("📝 Job Description")
job_description = st.text_area("Enter the job description:")

# Upload Resumes
st.header("📤 Upload Resumes (PDF)")
uploaded_files = st.file_uploader("Upload multiple resumes", type=["pdf"], accept_multiple_files=True)

if uploaded_files and job_description:
    resumes = []
    resume_names = []

    # Extract text from each uploaded resume
    for file in uploaded_files:
        resume_text = extract_text_from_pdf(file)
        if resume_text:
            resumes.append(resume_text)
            resume_names.append(file.name)
        else:
            st.error(f"⚠️ Could not extract text from {file.name}. Try another file.")

    if resumes:
        # Vectorize job description and resumes
        tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        documents = [job_description] + resumes
        vectors = tfidf_vectorizer.fit_transform(documents).toarray()

        # Compute similarity scores
        job_vector = vectors[0].reshape(1, -1)
        resume_vectors = vectors[1:]
        scores = cosine_similarity(job_vector, resume_vectors).flatten()

        # Display ranked resumes
        results = pd.DataFrame({"Resume": resume_names, "Match Score": scores})
        results = results.sort_values(by="Match Score", ascending=False)

        st.subheader("📊 Ranked Candidates")
        st.dataframe(results)
