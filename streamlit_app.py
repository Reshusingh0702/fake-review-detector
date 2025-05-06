import streamlit as st
import joblib
import re
import string

# Load model and vectorizer
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Remove from final deployment!!!
assert model and vectorizer is not None

# Input text sanitization
def clean_text(text):
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)  # remove HTML tags
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)  # remove punctuation
    text = re.sub(r'\d+', '', text)  # remove numbers
    text = re.sub(r'\s+', ' ', text).strip()  # remove extra spaces
    return text

# UI Layout
st.set_page_config(page_title="🕵️ Fake Review Detector", layout="centered")

st.markdown("<h1 style='text-align: center;'>🕵️ Fake Review Detection System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter a review to check if it seems <b>genuine</b> or <b>fake</b>.</p>", unsafe_allow_html=True)

# Input
user_input = st.text_area("✍️ Enter Review Text:", height=200, placeholder="Type or paste a product/service review here...")

# Button
if st.button("🔍 Analyze Review"):
    if not user_input.strip():
        st.warning("⚠️ Please enter a review before analyzing.")
    else:
        with st.spinner("Analyzing the review... ⏳"):
            cleaned_review = clean_text(user_input)
            vectorized_review = vectorizer.transform([cleaned_review])
            prediction = model.predict(vectorized_review)[0]
            prediction_proba = model.predict_proba(vectorized_review)[0]

        st.success("✅ Analysis Complete!")

        if prediction == 1:
            st.markdown("<h4 style='color:green;'>🟢 This review is likely <b>genuine</b>.</h4>", unsafe_allow_html=True)
        else:
            st.markdown("<h4 style='color:red;'>🔴 This review is likely <b>fake</b>.</h4>", unsafe_allow_html=True)

        st.markdown(f"**🧠 Confidence:** `{round(max(prediction_proba) * 100, 2)}%`")

# Footer
st.markdown("---")
st.markdown("📘 *Model trained on real-world review data for binary classification of authenticity.*")
