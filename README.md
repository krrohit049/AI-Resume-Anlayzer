📄 AI Resume Analyzer

Smart web app to analyze resumes and job descriptions using AI. Get keyword matching, strengths, missing skills, and improvement suggestions instantly.

🚀 Features

📤 Resume Upload: Supports PDF & DOCX files

🧾 Job Description Input: Paste any JD to compare

🎯 Keyword Matching: Shows matched ✅ and missing ❌ keywords

🤖 AI Suggestions: GPT-powered feedback on improvements

📊 Resume Scoring: Technical & ATS-like score

💻 Responsive Design: Works perfectly on desktop & mobile

🛠️ Tech Stack

Frontend / UI: Streamlit

Backend / Processing: Python

Libraries: PyMuPDF, python-docx, NLTK, scikit-learn, NumPy

AI: OpenAI GPT API

⚡ Installation
# Clone the repo
git clone https://github.com/krrohit049/ai-resume-analyzer.git
cd ai-resume-analyzer

# (Optional) Create a virtual environment
python -m venv venv

source venv/bin/activate  # Linux/Mac

venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py



Note: Set your OpenAI API key in the app or as an environment variable.


📝 Usage

Upload your resume (PDF or DOCX)

Paste the job description

View:

Extracted resume text

Keyword similarity score

Matched & missing keywords

AI-generated feedback and scoring
