import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 标题
st.title("California Housing Data (1990) by 陈馨怡")

# 读取数据
df = pd.read_csv("housing.csv")

# 房价滑块
min_house_val = st.slider("Minimal Median House Value", min_value=0, max_value=500001, value=200000)
filtered_df = df[df["median_house_value"] >= min_house_val]

# 子标题
st.subheader("See more filters in the sidebar:")

# 侧边栏
with st.sidebar:
    location_options = df["ocean_proximity"].unique()
    selected_locations = st.multiselect("Choose the location type", location_options, default=location_options)
    income_choice = st.radio("Choose income level", ["Low", "Medium", "High"])

# 根据多选框筛选区位
filtered_df = filtered_df[filtered_df["ocean_proximity"].isin(selected_locations)]

# 根据单选框筛选收入区间
if income_choice == "Low":
    filtered_df = filtered_df[filtered_df["median_income"] <= 2.5]
elif income_choice == "Medium":
    filtered_df = filtered_df[(filtered_df["median_income"] > 2.5) & (filtered_df["median_income"] < 4.5)]
elif income_choice == "High":
    filtered_df = filtered_df[filtered_df["median_income"] >= 4.5]

# 绘制筛选后区域的地图
st.map(filtered_df)

# 房价直方图，30个分组
fig, ax = plt.subplots()
ax.hist(filtered_df["median_house_value"], bins=30)
ax.set_xlabel("Median House Value")
ax.set_ylabel("Count")
st.pyplot(fig)
