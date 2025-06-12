import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="データ分析（相関・回帰）")
st.title("📉 データ分析（相関分析・回帰分析）")

# CSVデータの読み込み（キャッシュ利用）
@st.cache_data
def load_data():
    df = pd.read_csv("data/sample_data.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df

df = load_data()

# データ表示
st.subheader("📋 元データの表示")
st.write(df)

# 相関分析（Correlation）
st.subheader("🔍 相関分析")

corr_matrix = df[['sales', 'expenses']].corr()
st.write("**相関行列**")
st.write(corr_matrix)

# 回帰分析（Linear Regression）
st.subheader("📈 回帰分析")

X = df[['expenses']].values.reshape(-1, 1)  # 説明変数（経費）
y = df['sales'].values  # 目的変数（売上）

# 回帰モデル作成・学習
model = LinearRegression()
model.fit(X, y)

# 結果を表示
coef = model.coef_[0]
intercept = model.intercept_

st.write("**回帰モデル（売上 = 経費 × 係数 + 切片）**")
st.write(f"- 係数 (Coefficient)：{coef:.2f}")
st.write(f"- 切片 (Intercept)：{intercept:.2f}")

# 回帰直線のプロット
fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(X, y, color='blue', label='実際のデータ')
ax.plot(X, model.predict(X), color='red', linewidth=2, label='回帰直線')
ax.set_xlabel('経費 (expenses)')
ax.set_ylabel('売上 (sales)')
ax.set_title('経費と売上の回帰分析')
ax.legend()
ax.grid(True)

st.pyplot(fig)
