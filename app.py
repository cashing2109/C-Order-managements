import streamlit as st

st.title("📊 Coffee Shop Live Orders")
st.write("### Enter a New Order")

# Input fields for order details
item_name = st.text_input("☕ Enter the coffee name:")
item_price = st.number_input("💰 Enter the price:", min_value=0.1, max_value=100.0, step=0.1)

if st.button("📩 Submit Order"):
    if item_name and item_price:
        st.success(f"✅ Order Received: {item_name} - ${item_price}")
    else:
        st.error("⚠ Please enter a valid item name and price!")

st.write("### More orders will appear here as they are placed...")
