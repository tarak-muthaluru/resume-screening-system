from sentence_transformers import SentenceTransformer
import numpy as np

# Load model once
print("Loading model...")
model = SentenceTransformer("all-MiniLM-L6-v2")
print("Model loaded.")


def get_embedding(text: str):
    """
    Convert text into a numeric embedding vector.
    Returns a numpy array of length 384.
    """
    return model.encode(text, convert_to_tensor=False)

def similarity(a_emb, b_emb) -> float:
    """
    Compute cosine similarity between two embedding vectors.
    Returns a float (usually between 0 and 1 for these models).
    """
    a = np.array(a_emb)
    b = np.array(b_emb)

    # Handle edge case: if any vector is all zeros
    if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
        return 0.0

    cos_sim = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    return float(cos_sim)
