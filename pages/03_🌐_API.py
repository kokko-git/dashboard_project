import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="外部APIデータ取得")
st.title("🌐 外部APIデータ取得")

@st.cache_data
def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else []

data = fetch_data()
df_api = pd.DataFrame(data)

st.subheader("📋 API取得データ（一部）")
st.write(df_api.head(10))

selected_id = st.selectbox("投稿ID選択", df_api["id"])
selected_post = df_api[df_api["id"] == selected_id].iloc[0]

st.write(f"### {selected_post['title']}")
st.write(selected_post["body"])
