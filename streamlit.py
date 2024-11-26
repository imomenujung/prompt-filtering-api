import streamlit as st
from sentence_transformers import SentenceTransformer, util
import json

# Load model for embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load keywords from JSON file
def load_filter_keywords():
    with open("filter_keywords.json", "r") as file:
        return json.load(file)["keywords"]

# Function to check prompt safety using embeddings
def is_prompt_safe_with_embeddings(prompt, keywords, threshold=0.7):
    # Compute embeddings
    prompt_embedding = model.encode(prompt, convert_to_tensor=True)
    keyword_embeddings = model.encode(keywords, convert_to_tensor=True)

    # Compute cosine similarity
    similarities = util.cos_sim(prompt_embedding, keyword_embeddings)

    # Check if any similarity exceeds the threshold
    for sim in similarities[0]:
        if sim > threshold:
            return False
    return True

# Function to check if prompt contains any keyword
def contains_keywords(prompt, keywords):
    for keyword in keywords:
        if keyword.lower() in prompt.lower():
            return True
    return False

# Streamlit UI
st.title("Prompt Filtering API")
st.write("Check if your input prompt is safe.")

# User input
prompt = st.text_area("Enter your prompt:", "")

# Check button
if st.button("Check Safety"):
    if prompt.strip() == "":
        st.error("Please enter a prompt!")
    else:
        keywords = load_filter_keywords()
        safe = is_prompt_safe_with_embeddings(prompt, keywords) and not contains_keywords(prompt, keywords)

        if safe:
            st.success("✅ Prompt is safe!")
        else:
            st.error("⚠️ Prompt is not safe!")
