import streamlit as st
import pandas as pd

#页面标题，把 [Your Name] 换成你的名字！
st.title("California Housing Data (1990) by [陈馨怡]")

#读取csv数据
df = pd.read_csv("housing.csv")

# 滑块：最低房屋中位数价格
min_house_val = st.slider("Minimal Median House Value", min_value=0, max_value=500001, value=200000)

# 筛选：只保留房价 >= 滑块值的数据
filtered_df = df[df["median_house_value"] >= min_house_val]

st.subheader("See more filters in the sidebar:")

# 侧边栏
with st.sidebar:
    # 获取所有区位类型
    location_options = df["ocean_proximity"].unique()
    # 多选框，默认全部选中
    selected_locations = st.multiselect("Choose the location type", location_options, default=location_options)
    # 收入单选按钮
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
st.histogram(filtered_df["median_house_value"], bins=30)
