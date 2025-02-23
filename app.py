import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Coffee options with prices (with size info)
coffee_menu = {
    "Latte (16 oz)": 4.99,
    "Espresso (16 oz)": 2.99,
    "Cappuccino (16 oz)": 3.99,
    "Mocha (16 oz)": 5.49,
    "Americano (16 oz)": 3.49,
    "Macchiato (16 oz)": 4.29
}

# Ensure persistent storage for sales data
sales_data_file = "sales_data.csv"
if not os.path.exists(sales_data_file):
    pd.DataFrame(columns=["Coffee", "Quantity", "Total Price"]).to_csv(sales_data_file, index=False)

# Load existing sales data
sales_data = pd.read_csv(sales_data_file)

# Global variables to track orders
total_cups_sold = sales_data["Quantity"].sum() if not sales_data.empty else 0
total_revenue = sales_data["Total Price"].sum() if not sales_data.empty else 0

st.title("📊 Coffee Shop Live Orders")

st.write("### Select a Coffee Order")

# Dropdown for selecting coffee
selected_coffee = st.selectbox("☕ Choose a coffee:", list(coffee_menu.keys()))

# Automatically update price based on selection
coffee_price = coffee_menu[selected_coffee]
st.write(f"💰 Price: ${coffee_price:.2f}")

# Input field for quantity
item_quantity = st.number_input("📦 Enter quantity:", min_value=1, max_value=100, step=1)

if st.button("📩 Submit Order"):
    total_cups_sold += item_quantity
    total_revenue += coffee_price * item_quantity
    new_order = pd.DataFrame([[selected_coffee, item_quantity, coffee_price * item_quantity]], 
                              columns=["Coffee", "Quantity", "Total Price"])
    sales_data = pd.concat([sales_data, new_order], ignore_index=True)
    sales_data.to_csv(sales_data_file, index=False)
    st.success(f"✅ Order Received: {item_quantity}x {selected_coffee} - ${coffee_price * item_quantity:.2f}")

st.write("### Live Sales Report")
st.write(f"Total Cups Sold: {total_cups_sold}")
st.write(f"Total Revenue: ${total_revenue:.2f}")

# Visualization of sales trends
if not sales_data.empty:
    st.write("### Sales Trend")
    fig = px.bar(sales_data, x="Coffee", y="Quantity", title="Sales by Coffee Type", color="Coffee")
    st.plotly_chart(fig)

# Reset button to clear sales data
if st.button("🔄 Reset Sales Data"):
    total_cups_sold = 0
    total_revenue = 0.0
    sales_data = pd.DataFrame(columns=["Coffee", "Quantity", "Total Price"])
    sales_data.to_csv(sales_data_file, index=False)
    st.warning("⚠ Sales data has been reset!")

