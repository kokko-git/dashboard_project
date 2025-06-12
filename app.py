import streamlit as st
import pandas as pd
import requests

# ページタイトル
st.title("🌐 外部APIからデータを取得・表示")

# APIからデータを取得する関数（キャッシュ利用）
@st.cache_data
def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"APIからデータ取得に失敗しました。ステータスコード: {response.status_code}")
        return []

# データを取得
data = fetch_data()

# 取得したデータをpandasのDataFrameに変換
df_api = pd.DataFrame(data)

# 取得データ表示
st.subheader("📋 APIから取得したデータ（一部）")
st.write(df_api.head(10))

# 選択した投稿を詳細表示
st.subheader("🔍 投稿の詳細表示")

post_ids = df_api["id"].tolist()
selected_id = st.selectbox("表示したい投稿のIDを選択", post_ids)

selected_post = df_api[df_api["id"] == selected_id].iloc[0]

st.write(f"### {selected_post['title']}")
st.write(selected_post["body"])
