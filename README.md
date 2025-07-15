<<<<<<< HEAD
# 🏍️ Used Bike Price Prediction

This project predicts the selling price of used bikes using machine learning. It features a robust data cleaning and EDA pipeline, advanced feature engineering, a Random Forest regression model, and a Streamlit web app for interactive predictions.

---

## 📊 Problem Statement

Given a dataset of used bikes, the goal is to build a regression model that can accurately predict the selling price of a bike based on its specifications and condition.

---

## 🚀 Features
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering with categorical encoding
- Model training and evaluation
- Streamlit app for user-friendly price prediction

---

## 📁 Project Structure
```
used-bike-price-prediction/
│
├── data_loader.py              # Loads and cleans data
├── feature_engineering.py      # Feature creation & encoding
├── model.py                    # Trains the regression model
├── predictor.py                # Uses saved model to make predictions
├── streamlit_app.py            # Streamlit UI for price prediction
├── requirements.txt            # Python libraries needed
├── README.md                   # Project documentation
│
├── models/
│   └── bike_price_model.joblib # Trained ML model
│   └── encoder.joblib          # Trained encoder
│
└── notebooks/
    └── 01_eda_and_cleaning.ipynb # Data exploration & insights
```
---

## 🛠️ Getting Started

1. Clone the repo and install requirements:
   ```bash
   git clone https://github.com/<your-username>/used-bike-price-prediction.git
   cd used-bike-price-prediction
   pip install -r requirements.txt
   ```
2. Train the model:
   ```bash
   python model.py
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```

---

## 📄 License
MIT
=======
# used-bike-price-prediction
Used Bike Price Prediction – ML project to predict used bike prices. Includes data cleaning, EDA, feature engineering, Random Forest model, and a Streamlit app for interactive predictions. Clean pipeline, visual insights, and real-time predictions.
>>>>>>> 1800a8cd9fe5ae14cf737170531b322fd9c2f162
