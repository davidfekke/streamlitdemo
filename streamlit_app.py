import streamlit as st

def runspecialeffects():
    st.balloons()
    st.snow()

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.write("This is a new line added to the app.")

if st.button("Press me!"):
    runspecialeffects()

