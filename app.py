import streamlit as st

# Coffee options with prices
coffee_menu = {
    "Latte": 4.99,
    "Espresso": 2.99,
    "Cappuccino": 3.99,
    "Mocha": 5.49
}

# Global variables to track orders
total_cups_sold = 0
total_revenue = 0.0
orders = []

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
    st.success(f"✅ Order Received: {item_quantity}x {selected_coffee} - ${coffee_price * item_quantity:.2f}")

st.write("### Live Sales Report")
st.write(f"Total Cups Sold: {total_cups_sold}")
st.write(f"Total Revenue: ${total_revenue:.2f}")

st.write("### Recent Orders")
for order in orders[-5:]:  # Display last 5 orders
    st.write(order)
