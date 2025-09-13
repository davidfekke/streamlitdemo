import streamlit as st
import time

st.title("My Streamlit App")
st.write("Hello, world!")

if st.button("Do something!"):
    success_placeholder = st.empty()
    success_placeholder.success("Success!", icon="✅")
    time.sleep(5)
    success_placeholder.empty()

import pandas as pd

# open a dataframe to my people_data.csv
df = pd.read_csv("people_data.csv")

# display the dataframe
st.write(df)