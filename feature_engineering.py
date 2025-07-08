import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
import re
def extract_numeric(val):
    if pd.isnull(val): return np.nan
    val = str(val)
    match = re.search(r"[\d.]+", val.replace(",", ""))
    return float(match.group()) if match else np.nan
def engineer_features(df, fit_encoder=False, encoder=None):
    df = df.copy()
    if 'model_name' in df.columns:
        df['brand'] = df['model_name'].apply(lambda x: str(x).split()[0])
    if 'model_year' in df.columns:
        df['bike_age'] = 2025 - df['model_year']
    for col in ['mileage', 'power', 'price', 'kms_driven']:
        if col in df.columns:
            df[col] = df[col].apply(extract_numeric)
            df[col] = df[col].fillna(df[col].mean())
    df['brand'] = df['brand'].fillna('Unknown')
    if 'owner' in df.columns:
        df['owner'] = df['owner'].fillna('Unknown')
    df.drop_duplicates(inplace=True)
    drop_cols = [c for c in ['model_name', 'location'] if c in df.columns]
    df = df.drop(columns=drop_cols)
    cat_cols = [col for col in ['brand', 'owner'] if col in df.columns]
    num_cols = [col for col in df.columns if col not in cat_cols and col != 'price']
    if fit_encoder and cat_cols:
        encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
        cat_data = encoder.fit_transform(df[cat_cols])
        cat_feature_names = encoder.get_feature_names_out(cat_cols)
    elif encoder is not None and cat_cols:
        cat_data = encoder.transform(df[encoder.feature_names_in_])
        cat_feature_names = encoder.get_feature_names_out(encoder.feature_names_in_)
    else:
        cat_data = np.empty((len(df), 0))
        cat_feature_names = []
    num_data = df[num_cols].values if num_cols else np.empty((len(df), 0))
    all_data = np.hstack([num_data, cat_data])
    all_feature_names = num_cols + list(cat_feature_names)
    if 'price' in df.columns:
        all_data = np.hstack([all_data, df[['price']].values])
        all_feature_names.append('price')
    df_encoded = pd.DataFrame(all_data, columns=all_feature_names)
    df_encoded = df_encoded.apply(pd.to_numeric, errors='ignore')
    if fit_encoder:
        return df_encoded, encoder
    else:
        return df_encoded
