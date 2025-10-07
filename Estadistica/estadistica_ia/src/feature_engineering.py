import numpy as np
import pandas as pd

def time_features(df, ts_col='timestamp'):
    df = df.copy()
    df['hour'] = df[ts_col].dt.hour
    df['dayofweek'] = df[ts_col].dt.dayofweek
    df['is_weekend'] = df['dayofweek'] >= 5
    return df

def price_per_item(df):
    df = df.copy()
    df['price_per_item'] = df['price'] / df['quantity']
    return df
