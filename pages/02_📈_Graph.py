import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="インタラクティブグラフ")
st.title("📈 インタラクティブグラフ表示")

@st.cache_data
def load_data():
    df = pd.read_csv("data/sample_data.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df

df = load_data()

fig = px.line(
    df,
    x="date",
    y=["sales", "expenses"],
    labels={"value": "金額", "date": "日付", "variable": "項目"},
    title="売上と経費の推移"
)

fig.update_layout(hovermode="x unified")
st.plotly_chart(fig, use_container_width=True)
