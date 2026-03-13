import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask"

st.title("AI Router Chat Interface")

query = st.text_input("Enter your query")

if st.button("Submit"):

    if query:

        response = requests.post(
            API_URL,
            json={"query": query}
        )

        data = response.json()

        st.subheader("Response")

        st.write(data["response"])

        st.subheader("System Details")

        st.write(f"Model Used: {data['model_used']}")
        st.write(f"Complexity Level: {data['complexity_level']}")
        st.write(f"Confidence: {data['confidence']}")
        st.write(f"Latency: {data['latency']} seconds")
        st.write(f"Tokens Used: {data['tokens_used']}")
        st.write(f"Cost: ${data['cost']}")