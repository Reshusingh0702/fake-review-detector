import streamlit as st
import joblib
import re
import string
import os
from utils import get_response  # Clean import, no direct genai exposure



# # Load Model and Vectorizer

# def load_model_and_vectorizer(model_path, vectorizer_path):
#     try:
#         if not os.path.exists(model_path) or not os.path.exists(vectorizer_path):
#             raise FileNotFoundError("Model or vectorizer file not found.")
#         model = joblib.load(model_path)
#         vectorizer = joblib.load(vectorizer_path)
#         return model, vectorizer
#     except Exception as e:
#         st.error(f"❌ Error loading model or vectorizer: {e}")
#         st.stop()


# model, vectorizer = load_model_and_vectorizer("model_v1.pkl", "vectorizer_v0.pkl")



# # Input Text Sanitization

# def clean_text(text):
#     text = text.lower() 
#     text = re.sub(r"<.*?>", "", text)
#     text = re.sub(r"[%s]" % re.escape(string.punctuation), "", text)
#     text = re.sub(r"\d+", "", text)
#     text = re.sub(r"\s+", " ", text).strip()
#     return text 


# Page Config & Custom Styles

st.set_page_config(page_title="🕵 Fake Review Detector", layout="centered") 

st.markdown(
    """
    <style>
    body {
        background-color: #0e1117;
    }
    .stTextArea textarea {
        font-size: 16px;
        font-family: 'Courier New', monospace;
    }
    .result-box {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #1c1f26;
        margin-top: 1rem;
        text-align: center;
    }
    .footer {
        text-align: center;
        font-size: 15px;
        color: #a0a0a0;
        margin-top: 2rem;
        border-top: 1px solid #333;
        padding-top: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Title & Instructions

st.title("🕵 Review Summarizer (detector)")
st.markdown(
    "<p style='text-align: center; font-size: 18px;'>Enter a product or service review to get a prediction of review as <span style='color: #0E2148;'> Fake </span> or <span style='color: #0E2148;'> Genuine.</span></p>",
    unsafe_allow_html=True,
)
st.info("💡 Longer, detailed reviews yield more interesting summaries.")


# Review Input Form

with st.form("review_form"):
    user_input = st.text_area(
        "✍ Review Text:",
        height=115,
        placeholder="Type or paste a product/service review here...",
    )
    submitted = st.form_submit_button("🔍 analyze Review")


#output only

if submitted:
    if not user_input.strip():
        st.warning("⚠ Please enter a review before analyzingg.")
    else:
        try:
            with st.spinner("analyzing the review... ⏳"):
                output = get_response(user_input)
            st.markdown(
                f"""
                <div class="result-box" style="border-left: 5px solid #2196F3;">
                    <h4 style="color: #2196F3; margin-bottom: 0.5rem;"> Summary</h4>
                    <p style="font-size: 15px;color:#fff;">{output}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        except Exception as e:
            st.error(f"❌ An error occurred during summarization: {e}") 





# Analysis Results

# ...existing code...

if submitted:
    if not user_input.strip():
        st.warning("⚠ Please enter a review before analyzing.")
    else:
        try:
            with st.spinner("analyzing the review... ⏳"):
                # --- Skip fake review detection logic ---
                # cleaned_review = clean_text(user_input)
                # vectorized_review = vectorizer.transform([cleaned_review])
                # prediction = model.predict(vectorized_review)[0]
                # prediction_proba = model.predict_proba(vectorized_review)[0]

                # result_color = "#4CAF50" if prediction == 1 else "#F44336"
                # result_label = "🟢 Genuine" if prediction == 1 else "🔴 Fake"
                # confidence = round(max(prediction_proba) * 100, 2)

                # st.markdown(
                #     f"""
                #     <div class="result-box" style="border-left: 5px solid {result_color};">
                #         <h3 style="color: {result_color}; margin-bottom: 0.5rem;">{result_label}</h3>
                #         <p style="font-size: 16px;">🧠 <b>Confidence:</b> {confidence}%</p>
                #     </div>
                #     """,
                #     unsafe_allow_html=True,
                # )

                # --- Only Gemini output ---
                output = get_response(user_input)
                st.markdown(
                    f"""
                    <div class="result-box" style="border-left: 5px solid #2196F3;">
                        <h4 style="color: #2196F3; margin-bottom: 0.5rem;">streamlit Output</h4>
                        <p style="font-size: 15px;color:#fff;">{output}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        except Exception as e:
            st.error(f"❌ An error occurred during analysis: {e}")
# ...existing code...

# Footer section

st.markdown(
    """
    <div class="footer">
        🛠 Built with <b>Streamlit</b> 
        🔗 <a href="https://github.com/Reshusingh0702/fake-review-detector" target="_blank" style="color: #ccc;">
        View on GitHub</a>
    </div>
    """,
    unsafe_allow_html=True,
)