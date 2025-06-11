import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# matplotlibの日本語対応（メイリオを指定）
plt.rcParams['font.family'] = 'Meiryo'

# ページタイトル
st.title("📊 データ可視化ダッシュボード（統計・グラフ表示）")

# CSVデータ読み込み（キャッシュで効率化）
@st.cache_data
def load_data():
    data = pd.read_csv("data/sample_data.csv")
    data["date"] = pd.to_datetime(data["date"])
    return data

df = load_data()

# データ表示
st.subheader("📋 元データの表示")
st.write(df)

# 基本統計表示
st.subheader("📐 基本統計情報")

sales_stats = df["sales"].agg(["mean", "median", "max", "min"])
expenses_stats = df["expenses"].agg(["mean", "median", "max", "min"])

col1, col2 = st.columns(2)

with col1:
    st.markdown("**売上(sales)**")
    st.write(sales_stats)

with col2:
    st.markdown("**経費(expenses)**")
    st.write(expenses_stats)

# グラフ表示
st.subheader("📈 売上と経費の推移（折れ線グラフ）")

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(df["date"], df["sales"], marker="o", linestyle="-", color="blue", label="売上 (sales)")
ax.plot(df["date"], df["expenses"], marker="x", linestyle="--", color="red", label="経費 (expenses)")

ax.set_xlabel("日付 (Date)")
ax.set_ylabel("金額 (Amount)")
ax.set_title("売上・経費の推移")
ax.legend()
ax.grid(True)

st.pyplot(fig)
