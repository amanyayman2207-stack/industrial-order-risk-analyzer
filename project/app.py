import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(page_title="Supply Chain Delay Predictor", page_icon="🚚", layout="centered")

# Load the trained pipeline
@st.cache_resource
def load_model():
    return joblib.load("late_delivery_pipeline.pkl")

model = load_model()

# App Header
st.title("🚚 Industrial Supply Chain Late-Delivery Predictor")
st.markdown("""
Predict whether an incoming manufacturing/dispatch order is at high risk of *late delivery* before dispatch, enabling proactive production scheduling and client communication.
""")

st.divider()

# User Input Form
st.subheader("📋 Enter Order & Dispatch Details")

col1, col2 = st.columns(2)

with col1:
    shipping_mode = st.selectbox(
        "Shipping Mode",
        ["Standard Class", "First Class", "Second Class", "Same Day"]
    )
    scheduled_days = st.slider("Scheduled Dispatch Window (Days)", min_value=0, max_value=4, value=2)
    order_quantity = st.number_input("Order Item Quantity (Units)", min_value=1, max_value=50, value=3)
    sales_value = st.number_input("Order Sales Value ($)", min_value=10.0, max_value=5000.0, value=250.0, step=10.0)

with col2:
    payment_type = st.selectbox(
        "Transaction / Contract Type",
        ["DEBIT", "TRANSFER", "CASH", "PAYMENT"]
    )
    customer_segment = st.selectbox(
        "Customer Segment",
        ["Consumer", "Corporate", "Home Office"]
    )
    order_region = st.selectbox(
        "Destination Region",
        ["Western Europe", "Central America", "South America", "Oceania", "Southeast Asia", "Eastern Asia", "US Center", "West of USA"]
    )
    category_name = st.selectbox(
        "Product Category",
        ["Cleats", "Men's Footwear", "Women's Apparel", "Indoor/Outdoor Games", "Fishing", "Water Sports", "Camping & Hiking", "Shop By Sport"]
    )

# Feature Engineering (must match training pipeline exactly)
value_per_unit = sales_value / (order_quantity + 1e-5)

# Create input DataFrame
input_data = pd.DataFrame({
    'Days for shipment (scheduled)': [scheduled_days],
    'Order Item Quantity': [order_quantity],
    'Sales': [sales_value],
    'Value_per_Unit': [value_per_unit],
    'Type': [payment_type],
    'Category Name': [category_name],
    'Customer Segment': [customer_segment],
    'Order Region': [order_region],
    'Shipping Mode': [shipping_mode]
})

st.divider()

# Prediction Button
if st.button("🔍 Predict Delivery Risk", type="primary", use_container_width=True):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ *HIGH RISK OF LATE DELIVERY* (Risk Probability: {probability:.1%})")
        st.markdown("*Recommended Action:* Flag order for priority production line allocation or proactively notify the client to adjust delivery expectations.")
    else:
        st.success(f"✅ *ON-TIME DELIVERY EXPECTED* (Delay Risk Probability: {probability:.1%})")
        st.markdown("*Recommended Action:* Proceed with standard dispatch scheduling.")