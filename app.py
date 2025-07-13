
import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load('fake_news_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# App title
st.title("📰 Indian Health Fake News Detector")
st.markdown("Enter a health-related news headline to check if it's **Real** or **Fake**.")

# User input
user_input = st.text_area("🧾 Enter News Headline")

# Prediction logic
if st.button("🔍 Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a news headline.")
    else:
        vec = vectorizer.transform([user_input])
        prediction = model.predict(vec)[0]
        if prediction == 1:
            st.success("✅ Real News")
        else:
            st.error("❌ Fake News")
