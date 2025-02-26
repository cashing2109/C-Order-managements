import streamlit as st
import pandas as pd
import plotly.express as px
import os
import datetime
import pytz

# Coffee options with prices and operating costs
coffee_menu = {
    "Latte (16 oz)": {"price": 4.99, "cost": 2.00},
    "Espresso (16 oz)": {"price": 2.99, "cost": 1.00},
    "Cappuccino (16 oz)": {"price": 3.99, "cost": 1.50},
    "Mocha (16 oz)": {"price": 5.49, "cost": 2.50},
    "Americano (16 oz)": {"price": 3.49, "cost": 1.25},
    "Macchiato (16 oz)": {"price": 4.29, "cost": 1.75}
}

# Ensure persistent storage for sales data
sales_data_file = "sales_data.csv"
required_columns = ["Coffee", "Quantity", "Total Price", "Total Cost", "Profit"]
if not os.path.exists(sales_data_file):
    pd.DataFrame(columns=required_columns).to_csv(sales_data_file, index=False)

sales_data = pd.read_csv(sales_data_file)
for col in required_columns:
    if col not in sales_data.columns:
        sales_data[col] = 0

# Global variables to track orders
total_cups_sold = sales_data["Quantity"].sum() if not sales_data.empty else 0
total_revenue = sales_data["Total Price"].sum() if not sales_data.empty else 0
total_cost = sales_data["Total Cost"].sum() if not sales_data.empty else 0
total_profit = sales_data["Profit"].sum() if not sales_data.empty else 0

# Display the current date and time at the top-right corner
est = pytz.timezone('US/Eastern')
current_time = datetime.datetime.now(est).strftime("%m/%d/%Y, %I:%M:%S %p")
st.markdown(
    f"<div style='text-align: right; font-size: 16px; font-weight: bold;'>{current_time}</div>",
    unsafe_allow_html=True
)

st.markdown("""
    <h1 style='text-align: center;'>☕ Live Coffee Shop</h1>
    <p style='text-align: center; font-size: 18px;'><strong>Made by MD H. Rahman</strong></p>
    <p style='text-align: center;'><a href='https://www.linkedin.com/in/habib-rahmann/' target='_blank'>LinkedIn Profile</a></p>
""", unsafe_allow_html=True)

# Add creator name and LinkedIn profile
#st.write("**Made by MD H. Rahman**")
#st.markdown("[LinkedIn Profile](https://www.linkedin.com/in/habib-rahmann/)")

st.write("### Select a Coffee Order")
selected_coffee = st.selectbox("☕ Choose a coffee:", list(coffee_menu.keys()))
coffee_price = coffee_menu[selected_coffee]["price"]
st.write(f"💰 Price: ${coffee_price:.2f}")

item_quantity = st.number_input("📦 Enter quantity:", min_value=1, max_value=100, step=1)

if st.button("📩 Submit Order"):
    total_price = coffee_price * item_quantity
    total_cost_value = coffee_menu[selected_coffee]["cost"] * item_quantity
    profit = total_price - total_cost_value
    total_cups_sold += item_quantity
    total_revenue += total_price
    total_cost += total_cost_value
    total_profit += profit
    new_order = pd.DataFrame([[selected_coffee, item_quantity, total_price, total_cost_value, profit]], 
                              columns=required_columns)
    sales_data = pd.concat([sales_data, new_order], ignore_index=True)
    sales_data.to_csv(sales_data_file, index=False)
    st.success(f"✅ Order Received: {item_quantity}x {selected_coffee} - ${total_price:.2f}")

st.write("### Live Sales Report")
st.write(f"Total Cups Sold: {total_cups_sold}")
st.write(f"Total Revenue: ${total_revenue:.2f}")

# Sales comparison graph
if not sales_data.empty:
    st.write("### Sales Trend")
    fig = px.bar(sales_data, x="Coffee", y="Quantity", title="Sales by Coffee Type", color="Coffee")
    st.plotly_chart(fig)

# Reset button to clear sales data
if st.button("🔄 Reset Sales Data"):
    total_cups_sold = 0
    total_revenue = 0.0
    total_cost = 0.0
    total_profit = 0.0
    sales_data = pd.DataFrame(columns=required_columns)
    sales_data.to_csv(sales_data_file, index=False)
    st.warning("⚠ Sales data has been reset!")

# Backend Data Section
st.write("### Backend Data: Profit Analysis")
st.write(f"💰 Total Revenue: ${total_revenue:.2f}")
st.write(f"⚙ Total Operating Cost: ${total_cost:.2f}")
st.write(f"📈 Total Profit: ${total_profit:.2f}")

# Best-selling coffee of the day
if not sales_data.empty:
    best_seller = sales_data.groupby("Coffee")["Quantity"].sum().idxmax()
    best_seller_count = sales_data.groupby("Coffee")["Quantity"].sum().max()
    st.write(f"🏆 Best-Selling Coffee: {best_seller} ({best_seller_count} sold)")

# Text before download button
st.write("### Download Daily Sales Report")

# CSV download button
if not sales_data.empty:
    csv_file = "daily_sales_report.csv"
    sales_data.to_csv(csv_file, index=False)
    with open(csv_file, "rb") as file:
        st.download_button(
            label="📥 Download Report (CSV)",
            data=file,
            file_name="daily_sales_report.csv",
            mime="text/csv"
        )


