import streamlit as st
import pandas as pd
import plotly.express as px  # plotlyを追加

# ページタイトル
st.title("📊 データ可視化ダッシュボード（インタラクティブなグラフ表示）")

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

# ---------- ここから本日の追加部分（Plotlyグラフ表示） ----------

# インタラクティブな折れ線グラフの表示
st.subheader("📈 インタラクティブな売上と経費の推移グラフ")

fig = px.line(
    df,
    x="date",
    y=["sales", "expenses"],
    labels={"value": "金額", "date": "日付", "variable": "項目"},
    title="売上と経費の推移"
)

fig.update_layout(
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)
