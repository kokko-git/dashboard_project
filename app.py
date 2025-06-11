import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# タイトル表示
st.title("📊 CSVデータと統計・グラフ表示")

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

# 統計情報の表示
st.subheader("🔍 統計情報")

mean_sales = df['sales'].mean()
mean_expenses = df['expenses'].mean()

median_sales = df['sales'].median()
median_expenses = df['expenses'].median()

max_sales = df['sales'].max()
min_sales = df['sales'].min()

max_expenses = df['expenses'].max()
min_expenses = df['expenses'].min()

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

# ---------------------- 以下、本日追加する部分 ---------------------- #
# グラフ表示
st.subheader("📈 売上と経費の折れ線グラフ")

fig, ax = plt.subplots(figsize=(10,5))

ax.plot(df['date'], df['sales'], marker='o', linestyle='-', label='売上(sales)')
ax.plot(df['date'], df['expenses'], marker='x', linestyle='--', label='経費(expenses)')

ax.set_xlabel('日付 (Date)')
ax.set_ylabel('金額 (Amount)')
ax.set_title('売上と経費の推移')
ax.legend()

ax.grid(True)

st.pyplot(fig)
