import pandas as pd
import joblib
from feature_engineering import engineer_features
def load_model_and_predict(input_dict, model_path, encoder_path):
    model = joblib.load(model_path)
    encoder = joblib.load(encoder_path)
    df = pd.DataFrame([input_dict])
    X = engineer_features(df, fit_encoder=False, encoder=encoder)
    if 'price' in X.columns:
        X = X.drop('price', axis=1)
    prediction = model.predict(X)
    return prediction[0]
