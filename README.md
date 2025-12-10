\# Resume Screening System (ATS-style Semantic Matcher)



This project is an ATS-style Resume Screening System that automatically compares candidate resumes against a Job Description (JD) using semantic similarity. It uses modern NLP embeddings (Sentence Transformers) to understand meaning, not just keywords, and ranks multiple resumes based on how well they match the JD.



The system is built as an end-to-end pipeline and exposed through a Streamlit web application so that users can upload resumes, paste a JD, and instantly get match scores and rankings.



---



\## 🚀 Key Features



\- \*\*PDF Resume Parsing\*\*  

&nbsp; Extracts text from PDF resumes using a dedicated I/O module.



\- \*\*Semantic Matching using Embeddings\*\*  

&nbsp; Uses the `all-MiniLM-L6-v2` model from `sentence-transformers` to convert both JD and resumes into vector embeddings.



\- \*\*Cosine Similarity Scoring\*\*  

&nbsp; Computes similarity scores between JD and each resume using cosine similarity.



\- \*\*Section-wise Analysis (Skills \& Experience)\*\*  

&nbsp; Extracts approximate \*\*Skills\*\* and \*\*Experience\*\* sections from resume text and computes:

&nbsp; - Overall JD vs Resume score  

&nbsp; - JD Skills vs Resume Skills score  

&nbsp; - JD Responsibilities vs Resume Experience score  



\- \*\*Multi-Resume Ranking\*\*  

&nbsp; Supports multiple resume uploads and ranks them based on relevance to the JD.



\- \*\*Streamlit Web UI\*\*  

&nbsp; Interactive interface to:

&nbsp; - Paste or edit JD text  

&nbsp; - Upload one or more resume PDFs  

&nbsp; - View ranked results in a clean table with human-readable match labels.



---



\## 🧱 Project Architecture / Workflow



1\. \*\*Input\*\*  

&nbsp;  - User enters/pastes a Job Description (overall, skills, responsibilities).  

&nbsp;  - User uploads one or more resume PDFs via the Streamlit UI.



2\. \*\*PDF Text Extraction (`file\_io.py`)\*\*  

&nbsp;  - Reads each PDF file.  

&nbsp;  - Extracts raw text from all pages.



3\. \*\*Text Cleaning \& Section Extraction (`resume\_sections.py`)\*\*  

&nbsp;  - Normalizes whitespace and basic formatting.  

&nbsp;  - Heuristically identifies sections like:

&nbsp;    - Skills  

&nbsp;    - Work/Professional Experience  

&nbsp;  - Returns section-wise text for further processing.



4\. \*\*Embedding Generation (`embedding.py`)\*\*  

&nbsp;  - Loads `all-MiniLM-L6-v2` from `sentence-transformers`.  

&nbsp;  - Converts:

&nbsp;    - JD overall text  

&nbsp;    - JD skills text  

&nbsp;    - JD responsibilities text  

&nbsp;    - Full resume text  

&nbsp;    - Resume skills section  

&nbsp;    - Resume experience section  

&nbsp;  - into numeric vector embeddings.



5\. \*\*Similarity Computation (`embedding.py`)\*\*  

&nbsp;  - Uses cosine similarity to compute:

&nbsp;    - Overall match (JD full vs Resume full)  

&nbsp;    - Skills match (JD skills vs Resume skills)  

&nbsp;    - Experience match (JD responsibilities vs Resume experience)



6\. \*\*Ranking \& Display (`app.py`)\*\*  

&nbsp;  - Combines scores into a structured result set.  

&nbsp;  - Sorts resumes by overall similarity (descending).  

&nbsp;  - Displays:

&nbsp;    - Rank  

&nbsp;    - Resume file name  

&nbsp;    - Overall, Skills, Experience match as percentage + qualitative label (Excellent/Good/Weak/Poor).



---



\## 🛠 Tech Stack



\*\*Language \& Environment\*\*

\- Python 3.x

\- Virtual Environment (`venv`)



\*\*Core Libraries\*\*

\- \[`sentence-transformers`](https://www.sbert.net/) – semantic embeddings (`all-MiniLM-L6-v2`)

\- `torch` – backend for the embedding model

\- `numpy` – numerical operations and cosine similarity

\- PDF parsing library (`PyPDF2` / `pdfplumber` – depending on implementation)

\- `re` (Python regex) – text cleaning and section detection



\*\*Web UI\*\*

\- \[`streamlit`](https://streamlit.io/) – interactive web app for resume upload and scoring



\*\*Development \& Utilities\*\*

\- Jupyter Notebook – experimentation and prototyping

\- Git \& GitHub – version control and repository hosting



---



\## 📁 Project Structure



```text

resume-screen/

│

├── app.py                  # Streamlit app (UI + orchestration)

├── embedding.py            # Model loading, get\_embedding(), similarity()

├── file\_io.py              # PDF text extraction logic

├── resume\_sections.py      # Resume section extraction (skills, experience)

├── cleaning.py             # Text cleaning helpers (if used)

├── requirements.txt        # Python dependencies

├── jd.txt                  # Sample Job Description (optional)

│

├── sample\_data/            # Sample resumes and test files

│   ├── scanned\_resume.pdf.pdf

│   ├── resume\_pdf1.pdf.pdf

│   └── resume1.txt

│

├── cleaningpy.ipynb        # Notebook for text extraction \& cleaning experiments

├── similarity\_demo.ipynb   # Notebook for similarity experiments

├── test\_embedding.py       # Script to test embedding logic

├── test\_similarity.py      # Script to test similarity logic

├── test\_read\_txt.py        # Simple file reading tests

│

└── .gitignore              # Ignore virtual env, cache, temp files

\# Resume Screening System (ATS-style Semantic Matcher)



This project is an ATS-style Resume Screening System that automatically compares candidate resumes against a Job Description (JD) using semantic similarity. It uses modern NLP embeddings (Sentence Transformers) to understand meaning, not just keywords, and ranks multiple resumes based on how well they match the JD.



The system is built as an end-to-end pipeline and exposed through a Streamlit web application so that users can upload resumes, paste a JD, and instantly get match scores and rankings.



---



\## 🚀 Key Features



\- \*\*PDF Resume Parsing\*\*  

&nbsp; Extracts text from PDF resumes using a dedicated I/O module.



\- \*\*Semantic Matching using Embeddings\*\*  

&nbsp; Uses the `all-MiniLM-L6-v2` model from `sentence-transformers` to convert both JD and resumes into vector embeddings.



\- \*\*Cosine Similarity Scoring\*\*  

&nbsp; Computes similarity scores between JD and each resume using cosine similarity.



\- \*\*Section-wise Analysis (Skills \& Experience)\*\*  

&nbsp; Extracts approximate \*\*Skills\*\* and \*\*Experience\*\* sections from resume text and computes:

&nbsp; - Overall JD vs Resume score  

&nbsp; - JD Skills vs Resume Skills score  

&nbsp; - JD Responsibilities vs Resume Experience score  



\- \*\*Multi-Resume Ranking\*\*  

&nbsp; Supports multiple resume uploads and ranks them based on relevance to the JD.



\- \*\*Streamlit Web UI\*\*  

&nbsp; Interactive interface to:

&nbsp; - Paste or edit JD text  

&nbsp; - Upload one or more resume PDFs  

&nbsp; - View ranked results in a clean table with human-readable match labels.



---



\## 🧱 Project Architecture / Workflow



1\. \*\*Input\*\*  

&nbsp;  - User enters/pastes a Job Description (overall, skills, responsibilities).  

&nbsp;  - User uploads one or more resume PDFs via the Streamlit UI.



2\. \*\*PDF Text Extraction (`file\_io.py`)\*\*  

&nbsp;  - Reads each PDF file.  

&nbsp;  - Extracts raw text from all pages.



3\. \*\*Text Cleaning \& Section Extraction (`resume\_sections.py`)\*\*  

&nbsp;  - Normalizes whitespace and basic formatting.  

&nbsp;  - Heuristically identifies sections like:

&nbsp;    - Skills  

&nbsp;    - Work/Professional Experience  

&nbsp;  - Returns section-wise text for further processing.



4\. \*\*Embedding Generation (`embedding.py`)\*\*  

&nbsp;  - Loads `all-MiniLM-L6-v2` from `sentence-transformers`.  

&nbsp;  - Converts:

&nbsp;    - JD overall text  

&nbsp;    - JD skills text  

&nbsp;    - JD responsibilities text  

&nbsp;    - Full resume text  

&nbsp;    - Resume skills section  

&nbsp;    - Resume experience section  

&nbsp;  - into numeric vector embeddings.



5\. \*\*Similarity Computation (`embedding.py`)\*\*  

&nbsp;  - Uses cosine similarity to compute:

&nbsp;    - Overall match (JD full vs Resume full)  

&nbsp;    - Skills match (JD skills vs Resume skills)  

&nbsp;    - Experience match (JD responsibilities vs Resume experience)



6\. \*\*Ranking \& Display (`app.py`)\*\*  

&nbsp;  - Combines scores into a structured result set.  

&nbsp;  - Sorts resumes by overall similarity (descending).  

&nbsp;  - Displays:

&nbsp;    - Rank  

&nbsp;    - Resume file name  

&nbsp;    - Overall, Skills, Experience match as percentage + qualitative label (Excellent/Good/Weak/Poor).



---



\## 🛠 Tech Stack



\*\*Language \& Environment\*\*

\- Python 3.x

\- Virtual Environment (`venv`)



\*\*Core Libraries\*\*

\- \[`sentence-transformers`](https://www.sbert.net/) – semantic embeddings (`all-MiniLM-L6-v2`)

\- `torch` – backend for the embedding model

\- `numpy` – numerical operations and cosine similarity

\- PDF parsing library (`PyPDF2` / `pdfplumber` – depending on implementation)

\- `re` (Python regex) – text cleaning and section detection



\*\*Web UI\*\*

\- \[`streamlit`](https://streamlit.io/) – interactive web app for resume upload and scoring



\*\*Development \& Utilities\*\*

\- Jupyter Notebook – experimentation and prototyping

\- Git \& GitHub – version control and repository hosting



---



\## 📁 Project Structure



```text

resume-screen/

│

├── app.py                  # Streamlit app (UI + orchestration)

├── embedding.py            # Model loading, get\_embedding(), similarity()

├── file\_io.py              # PDF text extraction logic

├── resume\_sections.py      # Resume section extraction (skills, experience)

├── cleaning.py             # Text cleaning helpers (if used)

├── requirements.txt        # Python dependencies

├── jd.txt                  # Sample Job Description (optional)

│

├── sample\_data/            # Sample resumes and test files

│   ├── scanned\_resume.pdf.pdf

│   ├── resume\_pdf1.pdf.pdf

│   └── resume1.txt

│

├── cleaningpy.ipynb        # Notebook for text extraction \& cleaning experiments

├── similarity\_demo.ipynb   # Notebook for similarity experiments

├── test\_embedding.py       # Script to test embedding logic

├── test\_similarity.py      # Script to test similarity logic

├── test\_read\_txt.py        # Simple file reading tests

│

└── .gitignore              # Ignore virtual env, cache, temp files



