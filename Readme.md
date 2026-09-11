# Tx Fraud Predictor

An interactive machine learning web application built with Streamlit to predict and detect fraudulent financial transactions based on transfer amounts, transaction types, and account balances.

## Features

* **Real-Time Prediction:** Instantly classifies transactions as legitimate or potentially fraudulent using a pre-trained ML pipeline.
* **Interactive UI:** Dynamic input fields supporting transaction types, transfer amounts, and sender/receiver balance shifts.
* **Enhanced Visual Experience:** Integrated background media styling optimized for readability and modern aesthetic design.
* **Robust Pipeline Integration:** Uses serialized Scikit-Learn models (`.pkl`) to ensure seamless data preprocessing and inference consistency.

## Tech Stack

* **Frontend/UI:** Streamlit, HTML/CSS
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **Model Serialization:** Joblib / Pickle

## Project Structure

```text
tx-fraud-predictor/
│
├── fraud_detection.py           # Main Streamlit application script
├── fraud_detection_pipeline.pkl # Trained machine learning model pipeline
├── background.mp4               # Background video loop asset
├── .gitignore                   # Git exclusion rules
└── README.md                    # Project documentation