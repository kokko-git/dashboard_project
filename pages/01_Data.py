import streamlit as st
import pandas as pd

st.set_page_config(page_title="CSVデータと統計情報")
st.title("📊 CSVデータと統計情報")

@st.cache_data
def load_data():
    df = pd.read_csv("data/sample_data.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df

df = load_data()

st.subheader("📋 元データ")
st.write(df)

st.subheader("📐 統計情報")
stats = df.agg(["mean", "median", "max", "min"])
st.write(stats)
