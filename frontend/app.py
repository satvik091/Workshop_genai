import streamlit as st
import requests

# Connectivity to backend

backend_url = "http://127.0.0.1:8000/predict"

st.title("Sentiment Analysis App")
st.write("Enter text to analyze its sentiments...")

#Input user
user_input= st.text_area("Type Here...",height=150)

if st.button("Analyze"):
    if user_input.strip()=="":
        st.warning("Enter Something. Kuch to dal dlle!")
    else:
        response=requests.post(backend_url,json={"text":user_input})
        if response.status_code==200:
            result=response.json()
            st.success(f"Prediction- {result['label']} (Score: {result['score']:.2f})")
        else:
            st.error("Error: Nhi samjh paya! Koshish fir se kr")