import streamlit as st
import joblib
import re
import string

# Load the trained model and vectorizer
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

assert model and vectorizer is not None

# Input text sanitization
def clean_text(text):
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)  # remove HTML tags
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)  # remove punctuation
    text = re.sub(r'\d+', '', text)  # remove numbers
    text = re.sub(r'\s+', ' ', text).strip()  # remove extra spaces
    return text

# App Layout
st.set_page_config(page_title="Fake Review Detector", layout="centered")

st.title("🕵️ Fake Review Detection System")
st.markdown("Enter a review below to check whether it is likely to be **genuine** or **fake**.")

# Input text field
user_input = st.text_area("✍️ Review Text", height=200)

# Action button
if st.button("🔍 Analyze Review"):
    if not user_input.strip():
        st.warning("⚠️ Please enter a review.")
    else:
        cleaned_review = clean_text(user_input)
        vectorized_review = vectorizer.transform([cleaned_review])
        prediction = model.predict(vectorized_review)[0]
        prediction_proba = model.predict_proba(vectorized_review)[0]

        if prediction == 1:
            st.success("✅ This review is likely **genuine**.")
        else:
            st.error("🚨 This review is likely **fake**.")

        st.markdown(f"**Confidence:** {round(max(prediction_proba) * 100, 2)}%")

st.markdown("---")
st.markdown("📘 *This tool is powered by an ML model trained on labeled review data from Kaggle.*")
