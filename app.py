import streamlit as st
import pandas as pd

# タイトル表示
st.title("📊 CSVデータと統計情報の表示")

# CSVデータの読み込み
@st.cache_data
def load_data():
    data = pd.read_csv('data/sample_data.csv')
    data['date'] = pd.to_datetime(data['date'])
    return data

df = load_data()

# 元データの表示
st.subheader("📋 元データ")
st.write(df)

# 統計情報の表示（新規追加部分）
st.subheader("🔍 統計情報")

# 平均値
mean_sales = df['sales'].mean()
mean_expenses = df['expenses'].mean()

# 中央値
median_sales = df['sales'].median()
median_expenses = df['expenses'].median()

# 最大値・最小値
max_sales = df['sales'].max()
min_sales = df['sales'].min()

max_expenses = df['expenses'].max()
min_expenses = df['expenses'].min()

# 表示する
st.markdown("**売上(sales)**")
st.write(f"- 平均値: {mean_sales:.2f}")
st.write(f"- 中央値: {median_sales}")
st.write(f"- 最大値: {max_sales}")
st.write(f"- 最小値: {min_sales}")

st.markdown("**経費(expenses)**")
st.write(f"- 平均値: {mean_expenses:.2f}")
st.write(f"- 中央値: {median_expenses}")
st.write(f"- 最大値: {max_expenses}")
st.write(f"- 最小値: {min_expenses}")
