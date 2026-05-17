# =========================================================
# HOUSE PRICE PREDICTION STREAMLIT APP
# app.py
# =========================================================

import streamlit as st
import pandas as pd
import joblib
import numpy as np


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)


# =========================================================
# LOAD MODEL
# =========================================================

model = joblib.load("house_price_model.pkl")

model_columns = joblib.load("model_columns.pkl")


# =========================================================
# TITLE SECTION
# =========================================================

st.title("🏠 House Price Prediction System")

st.write(
    """
    Predict house prices instantly using Machine Learning.
    Fill in the details below and get estimated property value.
    """
)

st.divider()


# =========================================================
# USER INPUTS
# =========================================================

st.subheader("📋 Property Details")


# Area
area = st.slider(
    "Area (Square Feet)",
    500,
    10000,
    1500
)


# Bedrooms
bedrooms = st.slider(
    "Number of Bedrooms",
    1,
    10,
    3
)


# Bathrooms
bathrooms = st.slider(
    "Number of Bathrooms",
    1,
    10,
    2
)


# Floors
floors = st.slider(
    "Number of Floors",
    1,
    5,
    1
)


# Parking
parking = st.slider(
    "Parking Spaces",
    0,
    5,
    1
)


# Main Road
mainroad = st.selectbox(
    "Main Road Access",
    ["Yes", "No"]
)


# Guest Room
guestroom = st.selectbox(
    "Guest Room Available",
    ["Yes", "No"]
)


# Basement
basement = st.selectbox(
    "Basement Available",
    ["Yes", "No"]
)


# Air Conditioning
airconditioning = st.selectbox(
    "Air Conditioning",
    ["Yes", "No"]
)


# Preferred Area
prefarea = st.selectbox(
    "Preferred Area",
    ["Yes", "No"]
)


# Furnishing Status
furnishingstatus = st.selectbox(
    "Furnishing Status",
    [
        "Furnished",
        "Semi-Furnished",
        "Unfurnished"
    ]
)


st.divider()


# =========================================================
# PREDICT BUTTON
# =========================================================

if st.button("🔍 Predict House Price"):

    # =====================================================
    # CREATE INPUT DATA
    # =====================================================

    input_data = {
        'area': area,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'stories': floors,
        'parking': parking,
        'mainroad_yes': 1 if mainroad == "Yes" else 0,
        'guestroom_yes': 1 if guestroom == "Yes" else 0,
        'basement_yes': 1 if basement == "Yes" else 0,
        'airconditioning_yes': 1 if airconditioning == "Yes" else 0,
        'prefarea_yes': 1 if prefarea == "Yes" else 0,
        'furnishingstatus_semi-furnished': 1 if furnishingstatus == "Semi-Furnished" else 0,
        'furnishingstatus_unfurnished': 1 if furnishingstatus == "Unfurnished" else 0
    }


    # =====================================================
    # CREATE DATAFRAME
    # =====================================================

    input_df = pd.DataFrame([input_data])


    # =====================================================
    # HANDLE MISSING COLUMNS
    # =====================================================

    for col in model_columns:

        if col not in input_df.columns:

            input_df[col] = 0


    # =====================================================
    # COLUMN ORDER MATCHING
    # =====================================================

    input_df = input_df[model_columns]


    # =====================================================
    # PREDICTION
    # =====================================================

    prediction = model.predict(input_df)[0]


    # =====================================================
    # RESULT SECTION
    # =====================================================

    st.divider()

    st.subheader("🏡 Predicted House Price")


    st.success(
        f"Estimated Price: ₹ {round(prediction, 2):,}"
    )


    # =====================================================
    # PROPERTY SUMMARY
    # =====================================================

    st.subheader("📊 Property Summary")

    st.write(f"• Area: {area} sq.ft")
    st.write(f"• Bedrooms: {bedrooms}")
    st.write(f"• Bathrooms: {bathrooms}")
    st.write(f"• Floors: {floors}")
    st.write(f"• Parking: {parking}")


    # =====================================================
    # PRICE CATEGORY
    # =====================================================

    st.subheader("💡 Price Category")

    if prediction < 3000000:
        st.info("Budget Friendly Property")

    elif prediction < 7000000:
        st.warning("Mid-Range Property")

    else:
        st.error("Premium Luxury Property")


    # =====================================================
    # SIMPLE INSIGHTS
    # =====================================================

    st.subheader("📈 Why This Price?")

    reasons = []

    if area > 3000:
        reasons.append("Large property area")

    if bedrooms >= 4:
        reasons.append("Higher number of bedrooms")

    if bathrooms >= 3:
        reasons.append("More bathrooms increase value")

    if airconditioning == "Yes":
        reasons.append("Air conditioning available")

    if prefarea == "Yes":
        reasons.append("Located in preferred area")

    if furnishingstatus == "Furnished":
        reasons.append("Fully furnished property")

    if len(reasons) == 0:
        reasons.append("Standard property configuration")

    for reason in reasons:
        st.write(f"• {reason}")


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Built using Random Forest Regressor and Streamlit"
)