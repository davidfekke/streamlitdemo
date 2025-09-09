import streamlit as st

def makeitsnow():
    st.snow()

def birthdayeffects():
    st.balloons()

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.write("This is a new line added to the app.")

if st.button("Make it snow!"):
    makeitsnow()

if st.button("Celebrate my birthday!"):
    birthdayeffects()

