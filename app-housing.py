import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. App标题
st.title("California Housing Data (1990) by 陈馨怡")

# 读取数据集
df = pd.read_csv("housing.csv")

# 2. 房价滑块
min_house_val = st.slider("Minimal Median House Value", min_value=0, max_value=500001, value=200000)
filtered_df = df[df["median_house_value"] >= min_house_val]

# 3. 子标题
st.subheader("See more filters in the sidebar:")

# 侧边栏过滤器
with st.sidebar:
    # 4. 多选区位筛选，默认全选
    location_options = df["ocean_proximity"].unique()
    selected_locations = st.multiselect("Choose the location type", location_options, default=location_options)

    # 5. 收入单选按钮
    income_choice = st.radio("Choose income level", ["Low", "Medium", "High"])

# 应用区位筛选
filtered_df = filtered_df[filtered_df["ocean_proximity"].isin(selected_locations)]

# 应用收入筛选规则
if income_choice == "Low":
    filtered_df = filtered_df[filtered_df["median_income"] <= 2.5]
elif income_choice == "Medium":
    filtered_df = filtered_df[(filtered_df["median_income"] > 2.5) & (filtered_df["median_income"] < 4.5)]
elif income_choice == "High":
    filtered_df = filtered_df[filtered_df["median_income"] >= 4.5]

# 6. 绘制筛选后的地图
st.map(filtered_df)

# 7. 直方图，30 bins
fig, ax = plt.subplots()
ax.hist(filtered_df["median_house_value"], bins=30)
ax.set_xlabel("Median House Value")
ax.set_ylabel("Count")
st.pyplot(fig)
