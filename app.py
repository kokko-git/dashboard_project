import streamlit as st
import pandas as pd

# タイトル表示
st.title("📊 CSVデータの表示")

# CSVデータの読み込み
@st.cache_data
def load_data():
    data = pd.read_csv('data/sample_data.csv')
    data['date'] = pd.to_datetime(data['date'])
    return data

df = load_data()

# データの表示
st.subheader("元データの表示")
st.write(df)

# 統計情報の表示
st.subheader("データの統計情報")
st.write(df.describe())
