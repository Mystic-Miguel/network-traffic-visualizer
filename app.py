import streamlit as st, pandas as pd
st.title("Streamlit Starter")
uploaded = st.file_uploader("Upload CSV", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    st.write(df.head())
    st.bar_chart(df.select_dtypes("number"))
