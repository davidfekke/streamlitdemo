import streamlit as st
import pandas as pd

st.title("Pandas DataFrame Sample")

# open a dataframe to my people_data.csv
df = pd.read_csv("people_data.csv")

# display the dataframe
st.write(df)