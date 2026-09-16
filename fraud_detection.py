import streamlit as st
import pandas as pd
import joblib
import base64


def add_bg_video(video_file_path: str):
    """Encodes a local MP4 video and sets it as the background."""
    with open(video_file_path, "rb") as file:
        video_bytes = file.read()
    
    encoded_video = base64.b64encode(video_bytes).decode("utf-8")

    video_html = f"""
    <style>
    /* Make Streamlit's default background transparent */
    .stApp {{
        background: transparent;
    }}

    /* Position the video behind all app elements */
    #bg-video {{
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100vw;
        min-height: 100vh;
        width: 100vw;
        height: 100vh;
        object-fit: cover;
        z-index: -1;
        opacity: 0.25; /* Lower opacity keeps UI inputs readable */
        filter: brightness(0.6);
    }}
    </style>

    <video id="bg-video" autoplay loop muted playsinline>
        <source src="data:video/mp4;base64,{encoded_video}" type="video/mp4">
    </video>
    """
    st.markdown(video_html, unsafe_allow_html=True)


add_bg_video("background.mp4")


st.title("Fraud Detection Prediction App")
st.write("Please enter the transaction details and use the predict button")

model = joblib.load("fraud_detection_pipeline.pkl")

col1, col2 = st.columns(2)
with col1:
    transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT"])
with col2:
    amount = st.number_input("Amount", min_value=0.0, value=1000.0)

st.markdown("---")
st.subheader("Sender Details")

col3, col4 = st.columns(2)

with col3:
    oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0)
    if amount > oldbalanceOrg:
        st.error("You dont have sufficient balance in your account")
with col4:
    newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
    sender_final = oldbalanceOrg - amount
    if newbalanceOrig != sender_final:
        st.error("Mismatch in senders old and new balance")

st.markdown("---")
st.subheader("Reciever Details")

col5, col6 = st.columns(2)
with col5:
    oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
with col6:
    newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)
    receiver_final = oldbalanceDest + amount

    if newbalanceDest != receiver_final:
        st.error("Mismatch in sended and updated amount")

if st.button("Predict"):
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])


    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction : '{int(prediction)}'")

    if prediction == 1:
        st.error("This transaction can be fraud")
    else:
        st.success("This transaction looks like it is not a fraud")

