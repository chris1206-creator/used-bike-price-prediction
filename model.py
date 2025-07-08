import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
from feature_engineering import engineer_features
import numpy as np
def train_and_save_model(csv_path, model_path, encoder_path):
    df = pd.read_csv(csv_path)
    X, encoder = engineer_features(df, fit_encoder=True)
    y = X['price']
    X = X.drop('price', axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    try:
        rmse = mean_squared_error(y_test, model.predict(X_test), squared=False)
    except TypeError:
        rmse = np.sqrt(mean_squared_error(y_test, model.predict(X_test)))
    print(f"Test RMSE: {rmse:.2f}")
    joblib.dump(model, model_path)
    joblib.dump(encoder, encoder_path)
    print(f"Model saved to {model_path}")
    print(f"Encoder saved to {encoder_path}")
if __name__ == "__main__":
    train_and_save_model("D:/used-bike-price-prediction/bikes.csv", "models/bike_price_model.joblib", "models/encoder.joblib")
