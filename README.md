# AI Resume Screening Candidate Ranking-System
This project is an AI-powered Resume Screening and Candidate Ranking System that automates the recruitment process by evaluating and ranking resumes based on their relevance to a given job description.
Key Features:
Resume Parsing: Extracts text from uploaded PDF resumes.
TF-IDF Vectorization: Converts text data into numerical vectors for comparison.
Cosine Similarity Matching: Measures the similarity between job descriptions and resumes.
Candidate Ranking: Assigns a score to each resume based on relevance to the job description.
User-Friendly Interface: Built with Streamlit for easy interaction.
Technologies Used:
Python for backend processing
Streamlit for building the web-based user interface
pdfplumber for extracting text from PDFs
Scikit-learn (TF-IDF & Cosine Similarity) for text processing and ranking
How It Works:
Upload a job description.
Upload one or more resumes in PDF format.
The system processes the text and calculates similarity scores.
Resumes are ranked based on how well they match the job description.
The results are displayed in a structured format for easy comparison.
