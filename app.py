import streamlit as st

# ページのタイトルを設定
st.title('はじめてのデータ可視化ダッシュボード')

# シンプルなテキスト表示
st.write('これは最初のStreamlitアプリです。')

# ユーザー入力
name = st.text_input('名前を入力してください:')

# ボタンをクリックしたら表示
if st.button('挨拶する'):
    if name:
        st.success(f'こんにちは、{name}さん！')
    else:
        st.warning('名前を入力してください！')

