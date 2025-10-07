import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def generate_synthetic_ecommerce(n=20000, seed=42):
    np.random.seed(seed)
    start = datetime(2023,1,1)
    times = [start + timedelta(seconds=int(s)) for s in np.random.uniform(0, 365*24*3600, size=n)]
    user_id = np.random.randint(1, 10000, size=n)
    product_id = np.random.randint(1, 2000, size=n)
    prices = np.random.gamma(2.0, 20.0, size=n)
    outlier_idx = np.random.choice(n, size=max(1,int(0.005*n)), replace=False)
    prices[outlier_idx] *= 30
    quantity = np.random.poisson(1.6, size=n) + 1
    session_time = np.abs(np.random.normal(300, 200, size=n))
    latency = np.abs(np.random.exponential(scale=100, size=n))
    churn_prob = np.clip(0.02 + 0.00002*(prices- prices.mean()), 0, 1)
    churn = np.random.binomial(1, churn_prob)
    df = pd.DataFrame({
        'timestamp': times,
        'user_id': user_id,
        'product_id': product_id,
        'price': prices,
        'quantity': quantity,
        'session_time_s': session_time,
        'latency_ms': latency,
        'churn': churn
    })
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df
