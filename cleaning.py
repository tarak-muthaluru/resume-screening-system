# cleaning.py
import re

def clean_text(text):
    """
    Basic text cleaning:
    - Normalize whitespace
    - Remove extra newlines
    """
    text = re.sub(r"\s+", " ", text)
    text = text.strip()
    return text

