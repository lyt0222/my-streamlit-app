import streamlit as st

st.title("Welcome to My Streamlit App") 

name = st.text_input("Enter your name:")

if st.button("Submit"):
    st.write("Hello!", name)