from embedding import get_embedding, similarity

# 1) Three example texts
jd_like = "Looking for a data scientist with experience in Python and machine learning."
resume_like = "I am a data scientist skilled in Python, statistical modeling, and machine learning."
different_text = "I work as a sales executive focusing on client relationships and marketing campaigns."

# 2) Get embeddings
jd_emb = get_embedding(jd_like)
resume_emb = get_embedding(resume_like)
diff_emb = get_embedding(different_text)

# 3) Compute similarities
sim_jd_resume = similarity(jd_emb, resume_emb)
sim_jd_diff = similarity(jd_emb, diff_emb)

print("JD text:")
print(jd_like)
print("\nSimilar resume text:")
print(resume_like)
print("\nDifferent profile text:")
print(different_text)

print("\nJD vs Similar Resume similarity:", sim_jd_resume)
print("JD vs Different Profile similarity:", sim_jd_diff)
