import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache
def load_data():
    data = pd.read_csv('laptop_prices.csv')
    return data

df = load_data()

st.title('Laptop Price Dashboard')
st.markdown('## Visualize and Explore Laptop Prices')

st.write("### Laptop Data Preview")
st.dataframe(df.head()) 

brands = df['Company'].unique()
selected_brand = st.sidebar.multiselect('Select Laptop Brand(s)', brands, default=brands)

min_price, max_price = st.sidebar.slider('Select Price Range', int(df['Price_euros'].min()), int(df['Price_euros'].max()), (int(df['Price_euros'].min()), int(df['Price_euros'].max())))

filtered_data = df[(df['Company'].isin(selected_brand)) & (df['Price_euros'] >= min_price) & (df['Price_euros'] <= max_price)]

st.write(f"### Filtered Data ({len(filtered_data)} entries)")
st.dataframe(filtered_data)

st.write("### Price Distribution")
fig, ax = plt.subplots()
sns.histplot(filtered_data['Price_euros'], bins=20, ax=ax, color='skyblue')
ax.set_title('Price Distribution of Laptops')
st.pyplot(fig)

st.write("### Price by Brand")
fig, ax = plt.subplots(figsize=(10,6))
sns.boxplot(x='Company', y='Price_euros', data=filtered_data, ax=ax)
plt.xticks(rotation=45)
ax.set_title('Price Distribution by Brand')
st.pyplot(fig)

st.write("### Descriptive Statistics")
st.write(filtered_data.describe())

st.write("### Key Insights")
st.markdown("""
- Distribusi harga laptop berdasarkan brand.
- Pengguna bisa memilih rentang harga dan merk laptop sesuai keinginan.
- Visualisasi data meliputi distribusi harga dan boxplot harga per merk.
""")

st.sidebar.markdown("## About the App")
st.sidebar.text("This dashboard provides insights about laptop prices.")
