from embedding import get_embedding

text = "I am a data scientist with experience in Python and machine learning."

embedding = get_embedding(text)

print("Text:", text)
print("Type:", type(embedding))
print("Shape:", embedding.shape)
print("First 5 values:", embedding[:5])
