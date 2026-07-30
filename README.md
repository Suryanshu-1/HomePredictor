# 🏡 Housing Price Prediction App

A **Machine Learning web application** that predicts the estimated price of a house based on user-provided property details.

It uses a trained **Machine Learning Regression model** along with a complete **preprocessing pipeline** that handles missing values, feature scaling, and categorical feature encoding to generate accurate house price predictions.

---

## 🚀 Features

- Interactive UI with a clean and modern interface.
- Collects important house attributes:
  - Area (sq.ft)
  - Number of Bedrooms
  - Number of Bathrooms
  - Number of Stories
  - Main Road Access
  - Guest Room Availability
  - Basement Availability
  - Hot Water Heating
  - Air Conditioning
  - Parking Spaces
  - Preferred Area
  - Furnishing Status
- Automatic preprocessing of user inputs.
- Prediction using the **best-performing Regression model**.
- Instant house price estimation.

---

## 📂 Project Structure

```
├── Housing.csv             # Housing dataset
├── model.pkl               # Trained Regression model
├── train_model.py          # Model training script
├── app.py                  # Streamlit application
├── requirements.txt        # Project dependencies
└── README.md               # Documentation
```

---

## 🎯 Usage

1. Open the application here: **[Run the App]([YOUR_STREAMLIT_APP_LINK_HERE](https://homepredictor-r9n2ywjqvo7grmvh2ky34w.streamlit.app/))**
2. Enter the required house details.
3. Click **Predict House Price**.
4. View the estimated house price instantly.

---

## 🧠 Model Details

- **Problem Type:** Regression
- **Preprocessing:**
  - Missing Value Imputation
  - One-Hot Encoding
  - Standard Scaling
- **Train-Test Split:** 80 : 20
- **Model Selection:** Best model selected based on the highest **R² Score**

---

## ⚠️ Disclaimer

This application is intended for **educational and demonstration purposes only**.

The predicted prices are generated using a machine learning model trained on the provided dataset and should **not** be considered as official real estate valuations or financial advice.

---

## 📸 Screenshot


```text
<img width="1448" height="802" alt="image" src="https://github.com/user-attachments/assets/bcc5567d-b57a-4fa6-9fbd-834673d9cab0" />

```
---


## 🤝 Contribution

Pull requests are welcome. For any changes, please open an issue first to discuss what you would like to change.
