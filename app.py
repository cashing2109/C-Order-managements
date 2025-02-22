import streamlit as st
import time

st.title("📊 Coffee Shop Live Orders")

st.write("### Real-time order tracking")

# Simulated real-time output (can be replaced with actual C++ integration)
orders = [
    {"item": "Latte", "price": 4.99},
    {"item": "Espresso", "price": 2.99},
    {"item": "Cappuccino", "price": 3.99},
    {"item": "Mocha", "price": 5.49},
]

placeholder = st.empty()

for order in orders:
    with placeholder.container():
        st.success(f"☕ Order Received: {order['item']} - ${order['price']}")
    time.sleep(2)

st.write("### More orders will appear here...")
