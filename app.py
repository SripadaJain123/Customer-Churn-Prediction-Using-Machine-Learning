import streamlit as st
import pickle
import pandas as pd

# Load model
with open("random_forest_churn_model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Churn Prediction App", layout="centered")

st.title("📊 Customer Churn Prediction")
st.write("Enter customer details to predict churn")

# ===================== INPUTS =====================

Age = st.number_input("Age", min_value=18, max_value=100, value=30)
Gender = st.selectbox("Gender", ["Male", "Female", "Other"])

Membership_Years = st.number_input("Membership_Years", min_value=0.0, value=2.0)
Login_Frequency = st.number_input("Login_Frequency", value=10.0)
Session_Duration_Avg = st.number_input("Session_Duration_Avg", value=15.0)
Pages_Per_Session = st.number_input("Pages_Per_Session", value=5.0)

Cart_Abandonment_Rate = st.slider("Cart_Abandonment_Rate", 0.0, 1.0, 0.3)
Wishlist_Items = st.number_input("Wishlist_Items", min_value=0, value=3)
Total_Purchases = st.number_input("Total_Purchases", min_value=0, value=20)
Average_Order_Value = st.number_input("Average_Order_Value", value=2500.0)
Days_Since_Last_Purchase = st.number_input("Days_Since_Last_Purchase", min_value=0, value=15)

Discount_Usage_Rate = st.slider("Discount_Usage_Rate", 0.0, 1.0, 0.4)
Returns_Rate = st.slider("Returns_Rate", 0.0, 1.0, 0.1)
Email_Open_Rate = st.slider("Email_Open_Rate", 0.0, 1.0, 0.6)

Customer_Service_Calls = st.number_input("Customer_Service_Calls", min_value=0, value=1)
Product_Reviews_Written = st.number_input("Product_Reviews_Written", min_value=0, value=2)
Social_Media_Engagement_Score = st.number_input("Social_Media_Engagement_Score", value=50.0)

Mobile_App_Usage = st.selectbox("Mobile_App_Usage", [0, 1])
Payment_Method_Diversity = st.number_input("Payment_Method_Diversity", min_value=1, value=2)

Lifetime_Value = st.number_input("Lifetime_Value", value=100000.0)
Credit_Balance = st.number_input("Credit_Balance", value=5000.0)

# ===================== PREDICTION =====================

if st.button("Predict Churn"):

    input_df = pd.DataFrame([[
        Age,
        Gender,
        Membership_Years,
        Login_Frequency,
        Session_Duration_Avg,
        Pages_Per_Session,
        Cart_Abandonment_Rate,
        Wishlist_Items,
        Total_Purchases,
        Average_Order_Value,
        Days_Since_Last_Purchase,
        Discount_Usage_Rate,
        Returns_Rate,
        Email_Open_Rate,
        Customer_Service_Calls,
        Product_Reviews_Written,
        Social_Media_Engagement_Score,
        Mobile_App_Usage,
        Payment_Method_Diversity,
        Lifetime_Value,
        Credit_Balance
    ]], columns=[
        "Age",
        "Gender",
        "Membership_Years",
        "Login_Frequency",
        "Session_Duration_Avg",
        "Pages_Per_Session",
        "Cart_Abandonment_Rate",
        "Wishlist_Items",
        "Total_Purchases",
        "Average_Order_Value",
        "Days_Since_Last_Purchase",
        "Discount_Usage_Rate",
        "Returns_Rate",
        "Email_Open_Rate",
        "Customer_Service_Calls",
        "Product_Reviews_Written",
        "Social_Media_Engagement_Score",
        "Mobile_App_Usage",
        "Payment_Method_Diversity",
        "Lifetime_Value",
        "Credit_Balance"
    ])

    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.error("⚠️ Customer is likely to Churn")
    else:
        st.success("✅ Customer is NOT likely to Churn")
