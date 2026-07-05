import streamlit as st
import pandas as pd
import pickle

# ==============================
# CONFIG
# ==============================
THRESHOLD = 0.7

FEATURE_COLUMNS = [
    'Time','V1','V2','V3','V4','V5','V6','V7','V8','V9','V10',
    'V11','V12','V13','V14','V15','V16','V17','V18','V19',
    'V20','V21','V22','V23','V24','V25','V26','V27','V28','Amount'
]

# ==============================
# LOAD MODEL & SCALER (SAFE LOAD)
# ==============================
@st.cache_resource
def load_model():
    model = pickle.load(open("xgb_model.pkl", "rb"))
    scaler = pickle.load(open("xgb_scaler.pkl", "rb"))
    return model, scaler

model, scaler = load_model()

# ==============================
# UI SETUP
# ==============================
st.set_page_config(page_title="Fraud Detection", layout="wide")

st.title("💳 Credit Card Fraud Detection App")
st.markdown("Upload a CSV file to detect fraudulent transactions")

# Sidebar
st.sidebar.header("⚙️ Settings")
st.sidebar.write(f"Threshold: {THRESHOLD}")

# ==============================
# FILE UPLOAD
# ==============================
uploaded_file = st.file_uploader("📂 Upload CSV File", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Uploaded Data Preview")
    st.dataframe(df.head())

    # Remove target column if exists
    if "Class" in df.columns:
        df = df.drop("Class", axis=1)

    # Fix column order
    df = df.reindex(columns=FEATURE_COLUMNS)

    # Fill missing values
    df = df.fillna(0)

    # ==============================
    # PREDICTION
    # ==============================
    if st.button("🔍 Predict Fraud"):

        try:
            df_scaled = scaler.transform(df)
        except Exception as e:
            st.error(f"❌ Scaling Error: {e}")
            st.stop()

        probs = model.predict_proba(df_scaled)[:, 1]
        preds = (probs > THRESHOLD).astype(int)

        df["Fraud_Prob"] = probs
        df["Prediction"] = preds

        # ==============================
        # RESULTS
        # ==============================
        st.subheader("📊 Prediction Results")
        st.dataframe(df.head())

        # ==============================
        # SUMMARY
        # ==============================
        total = len(df)
        frauds = int(df["Prediction"].sum())
        fraud_percent = (frauds / total) * 100

        st.subheader("📈 Summary")

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Transactions", total)
        col2.metric("Fraud Detected", frauds)
        col3.metric("Fraud %", f"{fraud_percent:.2f}%")

        # ==============================
        # HIGH RISK TRANSACTIONS
        # ==============================
        st.subheader("🚨 High Risk Transactions (Top 5)")
        high_risk = df.sort_values(by="Fraud_Prob", ascending=False).head(5)
        st.dataframe(high_risk)

        # ==============================
        # DOWNLOAD BUTTON
        # ==============================
        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="⬇ Download Full Results",
            data=csv,
            file_name="fraud_predictions.csv",
            mime="text/csv"
        )