import streamlit as st
import os
from typing import List, Dict

from file_io import extract_pdf_text
from embedding import get_embedding, similarity
from resume_sections import extract_resume_sections  # NEW: for skills/experience sections

# ----- Page config -----
st.set_page_config(page_title="Resume Screening Demo - Day 4")

st.title("Resume Screening Demo - Day 4")
st.write("This app compares a Job Description (JD) with one or more resume PDFs and shows match scores (overall, skills, experience).")


# ----- Helper: human-readable score -----
def explain_score(score: float) -> str:
    """
    Convert similarity score (0..1) into percentage + label.
    If score is None, returns 'N/A'.
    """
    if score is None:
        return "N/A"

    percentage = score * 100

    if score >= 0.75:
        level = "Excellent"
        note = "Highly aligned with the JD."
    elif score >= 0.55:
        level = "Good"
        note = "Many skills match, but there may be some gaps."
    elif score >= 0.35:
        level = "Weak"
        note = "Partially aligned. Might not be the best fit."
    else:
        level = "Poor"
        note = "Mostly unrelated to the JD."

    return f"{percentage:.1f}% ({level}) – {note}"


def safe_emb(text: str):
    """Return embedding if text is non-empty, else None."""
    if not text:
        return None
    text = text.strip()
    if not text:
        return None
    return get_embedding(text)


# ----- Sidebar: resume upload -----
st.sidebar.header("Resume Input")

st.sidebar.write("Option: upload one or more resume PDFs")
uploaded_files = st.sidebar.file_uploader(
    "Upload resumes (.pdf)", type=["pdf"], accept_multiple_files=True
)

st.sidebar.write("---")
st.sidebar.write("If you don't upload anything, we will use the default sample resume.")
default_resume_path = "sample_data/scanned_resume.pdf.pdf"
st.sidebar.code(default_resume_path, language="text")


# ----- Main JD input area -----
st.subheader("Step 1: Enter / paste Job Description (JD) text")

# We split JD into full, skills, and responsibilities for section-wise scoring.
jd_full_default = """
We are looking for a data scientist with strong skills in Python, machine learning,
data analysis, and experience building classification and regression models.
The candidate should know Pandas, NumPy, statistics, and SQL.
"""

jd_skills_default = """
Required skills: Python, machine learning, data analysis, statistics, SQL,
experience with Pandas, NumPy, and building ML models for classification and regression.
"""

jd_resp_default = """
Responsibilities: build and deploy machine learning models, analyze large datasets,
create reports and dashboards, work with stakeholders to understand business problems,
and improve existing data pipelines.
"""

jd_full_text = st.text_area(
    "JD - Overall description:",
    value=jd_full_default.strip(),
    height=150,
)

with st.expander("Advanced: Edit JD skills and responsibilities sections used for section-wise scoring"):
    jd_skills_text = st.text_area(
        "JD - Skills section:",
        value=jd_skills_default.strip(),
        height=100,
    )
    jd_resp_text = st.text_area(
        "JD - Responsibilities / Experience section:",
        value=jd_resp_default.strip(),
        height=100,
    )

st.write("You can edit these JD texts and click the button below to compute match scores for each resume.")


# ----- Step 2: Compute scores for all resumes -----
if st.button("Compute match scores for resumes"):
    if not jd_full_text.strip():
        st.error("Please enter at least the overall JD description.")
    else:
        try:
            # 1) Decide which resumes to evaluate
            resume_entries: List[Dict] = []

            if uploaded_files:
                for uf in uploaded_files:
                    temp_path = f"temp_{uf.name}"
                    with open(temp_path, "wb") as f:
                        f.write(uf.getbuffer())
                    resume_entries.append({
                        "name": uf.name,
                        "path": temp_path,
                    })
                st.info(f"Using {len(resume_entries)} uploaded resume(s).")
            else:
                resume_entries.append({
                    "name": os.path.basename(default_resume_path),
                    "path": default_resume_path,
                })
                st.info(f"No uploads found. Using default resume: {default_resume_path}")

            # 2) Compute JD embeddings once
            st.write("Computing JD embeddings (overall, skills, experience)...")
            jd_full_emb = safe_emb(jd_full_text)
            jd_skills_emb = safe_emb(jd_skills_text)
            jd_resp_emb = safe_emb(jd_resp_text)

            # 3) For each resume, compute overall + section-wise similarity
            results = []
            for entry in resume_entries:
                path = entry["path"]
                name = entry["name"]

                if not os.path.exists(path):
                    st.warning(f"File not found, skipping: {path}")
                    continue

                # Extract resume text and sections
                full_text = extract_pdf_text(path)
                sections = extract_resume_sections(full_text)
                resume_skills_text = sections.get("skills", "")
                resume_exp_text = sections.get("experience", "")

                # Embeddings
                resume_full_emb = safe_emb(full_text)
                resume_skills_emb = safe_emb(resume_skills_text)
                resume_exp_emb = safe_emb(resume_exp_text)

                # Similarities (None if missing)
                overall = similarity(jd_full_emb, resume_full_emb) if (jd_full_emb is not None and resume_full_emb is not None) else None
                skills = similarity(jd_skills_emb, resume_skills_emb) if (jd_skills_emb is not None and resume_skills_emb is not None) else None
                experience = similarity(jd_resp_emb, resume_exp_emb) if (jd_resp_emb is not None and resume_exp_emb is not None) else None

                results.append({
                    "Resume": name,
                    "Overall": overall,
                    "Skills": skills,
                    "Experience": experience,
                })

            if not results:
                st.error("No valid resumes were processed.")
            else:
                # 4) Sort by overall score desc, keeping None at bottom
                results_sorted = sorted(
                    results,
                    key=lambda r: (r["Overall"] is None, -(r["Overall"] or 0.0))
                )

                st.success("Match scores computed successfully!")

                # 5) Build table data
                st.subheader("Ranking of resumes (Overall, Skills, Experience)")

                table_data = []
                for rank, item in enumerate(results_sorted, start=1):
                    table_data.append({
                        "Rank": rank,
                        "Resume": item["Resume"],
                        "Overall": explain_score(item["Overall"]),
                        "Skills": explain_score(item["Skills"]),
                        "Experience": explain_score(item["Experience"]),
                    })

                st.table(table_data)

        except Exception as e:
            st.error(f"An error occurred while processing: {e}")
