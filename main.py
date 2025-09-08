import streamlit as st

st.title("My Streamlit App")
st.write("Hello, world!")

user_input = st.text_input("Enter some text:")
st.write("You entered:", user_input)