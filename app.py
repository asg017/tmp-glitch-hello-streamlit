import streamlit as st
import pandas as pd

@st.cache
def getData():
    return  pd.read_csv('https://raw.githubusercontent.com/datadesk/la-weedmaps-analysis/master/data/vetted-la-dispensaries.csv')
st.header("Hello!")

st.text("wowza")

raw_data = getData();

st.line_chart(raw_data)

st.table(raw_data)
