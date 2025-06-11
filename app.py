import streamlit as st
import pandas as pd
import plotly.express as px

# タイトル表示
st.title("📊 インタラクティブなデータ可視化ダッシュボード（UI改善版）")

# CSVデータの読み込み（キャッシュ利用）
@st.cache_data
def load_data():
    data = pd.read_csv("data/sample_data.csv")
    data["date"] = pd.to_datetime(data["date"])
    return data

df = load_data()

# 日付範囲指定ウィジェット
st.sidebar.subheader("📅 日付範囲を指定")
min_date = df["date"].min()
max_date = df["date"].max()
date_range = st.sidebar.date_input(
    "表示する期間を選択",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# 項目選択ウィジェット
st.sidebar.subheader("🔎 表示項目を選択")
options = st.sidebar.multiselect(
    "データを選択してください",
    ["sales", "expenses"],
    ["sales", "expenses"]
)

# データフィルタリング
start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
filtered_df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

# 元データ表示
st.subheader("📋 フィルタ済みデータ")
st.write(filtered_df)

# 統計情報表示（選択項目のみ）
st.subheader("📐 選択したデータの統計情報")

stats = filtered_df[options].agg(["mean", "median", "max", "min"])
st.write(stats)

# インタラクティブなグラフ表示（選択項目のみ）
st.subheader("📈 インタラクティブなグラフ（選択項目）")

if options:
    fig = px.line(
        filtered_df,
        x="date",
        y=options,
        labels={"value": "金額", "date": "日付", "variable": "項目"},
        title="選択した項目の推移"
    )
    fig.update_layout(hovermode="x unified")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("⚠️ 左のメニューで表示項目を選択してください！")
