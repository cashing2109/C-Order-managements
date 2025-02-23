import streamlit as st
import pandas as pd
import plotly.express as px

# Coffee options with prices
coffee_menu = {
    "Latte": 4.99,
    "Espresso": 2.99,
    "Cappuccino": 3.99,
    "Mocha": 5.49,
    "Americano": 3.49,
    "Macchiato": 4.29
}

# Global variables to track orders
total_cups_sold = 0
total_revenue = 0.0
orders = []
order_data = pd.DataFrame(columns=["Coffee", "Quantity", "Total Price"])

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
    orders.append(f"{item_quantity}x {selected_coffee} - ${coffee_price * item_quantity:.2f}")
    new_order = pd.DataFrame([[selected_coffee, item_quantity, coffee_price * item_quantity]], columns=["Coffee", "Quantity", "Total Price"])
    order_data = pd.concat([order_data, new_order], ignore_index=True)
    st.success(f"✅ Order Received: {item_quantity}x {selected_coffee} - ${coffee_price * item_quantity:.2f}")

st.write("### Live Sales Report")
st.write(f"Total Cups Sold: {total_cups_sold}")
st.write(f"Total Revenue: ${total_revenue:.2f}")

st.write("### Recent Orders")
for order in orders[-5:]:  # Display last 5 orders
    st.write(order)

# Display data table of all orders
if not order_data.empty:
    st.write("### Order Data Table")
    st.dataframe(order_data)

# Visualization of sales trends
if not order_data.empty:
    st.write("### Sales Trend")
    fig = px.bar(order_data, x="Coffee", y="Quantity", title="Sales by Coffee Type", color="Coffee")
    st.plotly_chart(fig)

# Reset button to clear orders
if st.button("🔄 Reset Sales Data"):
    total_cups_sold = 0
    total_revenue = 0.0
    orders.clear()
    order_data = pd.DataFrame(columns=["Coffee", "Quantity", "Total Price"])
    st.warning("⚠ Sales data has been reset!")
