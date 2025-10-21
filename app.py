import streamlit as st
import fitz  # PyMuPDF
import docx
from openai import OpenAI

# --- OpenAI Client ---
client = OpenAI(api_key="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")

# --- Page Config ---
st.set_page_config(page_title="AI Resume Analyzer", layout="wide", page_icon="📄")

# --- Header ---
st.markdown("""
<style>
h1 {text-align: center; color: #1E90FF; font-size: 42px;}
h2 {color: #1E90FF;}
.metric-box {
    border-radius: 15px;
    padding: 20px;
    background: linear-gradient(135deg, #f0f8ff, #e6f2ff);
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>📄 AI Resume Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Upload Resume & Job Description for AI-powered insights</p>", unsafe_allow_html=True)

# --- Upload Columns ---
col1, col2 = st.columns([1,1])
with col1:
    resume_file = st.file_uploader("📤 Upload Resume (PDF or DOCX)", type=["pdf", "docx"])
with col2:
    job_desc = st.text_area("🧾 Paste Job Description", height=200)

# --- Main Processing ---
if resume_file and job_desc:
    # --- Extract Resume Text ---
    if resume_file.name.endswith(".pdf"):
        with fitz.open(stream=resume_file.read(), filetype="pdf") as pdf:
            text = "".join([page.get_text() for page in pdf])
    else:
        doc = docx.Document(resume_file)
        text = "\n".join([para.text for para in doc.paragraphs])

    st.subheader("📑 Extracted Resume Preview")
    st.text_area("Resume Content", text[:1500], height=200)

    # --- Keyword Match ---
    resume_text_lower = text.lower()
    job_keywords = [word.strip(".,:;!?()[]{}").lower() for word in job_desc.split() if len(word) > 2]

    matched_keywords = [kw for kw in job_keywords if kw in resume_text_lower]
    missing_keywords = [kw for kw in job_keywords if kw not in resume_text_lower]

    similarity = len(matched_keywords)/len(job_keywords) if job_keywords else 0
    score = similarity * 100

    # --- Display Keyword Score ---
    st.markdown(f"<div class='metric-box'><h2>🎯 Keyword Similarity Score: {score:.2f}%</h2></div>", unsafe_allow_html=True)

    # --- Matched / Missing Keywords Cards ---
    colA, colB = st.columns(2)
    with colA:
        st.markdown(f"<div class='metric-box'>✅ **Matched Keywords:**<br>{', '.join(matched_keywords) if matched_keywords else 'None'}</div>", unsafe_allow_html=True)
    with colB:
        st.markdown(f"<div class='metric-box'>❌ **Missing Keywords:**<br>{', '.join(missing_keywords) if missing_keywords else 'None'}</div>", unsafe_allow_html=True)

    # --- Quick Summary ---
    st.markdown("### 🌟 Quick Summary")
    if score >= 80:
        st.success("✅ Excellent Match! Your resume aligns very well with the job description.")
    elif score >= 60:
        st.warning("⚠️ Good Match. Try adding more relevant keywords to improve alignment.")
    else:
        st.error("❌ Low Match. Resume lacks essential keywords from the job description.")

    # --- GPT Feedback ---
    with st.spinner("🔍 Analyzing your resume with AI..."):
        prompt = f"""
        You are a professional ATS Resume Analyzer.
        Compare the following resume and job description.
        Provide:
        1. Missing keywords
        2. Strengths
        3. Improvement suggestions
        4. Give a score out of 100
        Resume: {text[:3000]}
        Job Description: {job_desc}
        """
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        analysis = response.choices[0].message.content

    st.subheader("🤖 AI Resume Feedback")
    st.write(analysis)

# --- Footer ---
st.markdown("---")
st.markdown("<p style='text-align:center;color:gray;'>💡 Created by Rohit </p>", unsafe_allow_html=True)
