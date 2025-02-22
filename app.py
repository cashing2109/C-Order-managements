import streamlit as st

# Global variables to track orders
total_cups_sold = 0
total_revenue = 0.0
orders = []

st.title("📊 Coffee Shop Live Orders")

st.write("### Enter a New Order")

# Input fields for order details
item_name = st.text_input("☕ Enter the coffee name:")
item_price = st.number_input("💰 Enter the price:", min_value=0.1, max_value=100.0, step=0.1)
item_quantity = st.number_input("📦 Enter quantity:", min_value=1, max_value=100, step=1)

if st.button("📩 Submit Order"):
    if item_name and item_price:
        total_cups_sold += item_quantity
        total_revenue += item_price * item_quantity
        orders.append(f"{item_quantity}x {item_name} - ${item_price * item_quantity:.2f}")
        st.success(f"✅ Order Received: {item_quantity}x {item_name} - ${item_price * item_quantity:.2f}")
    else:
        st.error("⚠ Please enter a valid item name and price!")

st.write("### Live Sales Report")
st.write(f"Total Cups Sold: {total_cups_sold}")
st.write(f"Total Revenue: ${total_revenue:.2f}")

st.write("### Recent Orders")
for order in orders[-5:]:  # Display last 5 orders
    st.write(order)
