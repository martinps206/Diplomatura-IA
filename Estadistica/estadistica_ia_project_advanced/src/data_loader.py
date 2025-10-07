import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def generate_large_synthetic(n=20000, seed=0):
    """
    Generador de dataset sintético orientado a e-commerce / series temporales.
    Devuelve un DataFrame con columnas:
      - timestamp
      - user_id
      - amount
      - price
      - quantity
      - base_demand (serie sintética con estacionalidad)
    Parámetros:
      - n: número de filas
      - seed: semilla aleatoria
    """
    np.random.seed(seed)
    start = datetime(2022,1,1)
    timestamps = [start + timedelta(minutes=int(i)) for i in range(n)]
    t = np.arange(n)
    # patrones estacionales
    daily = 10 + 5 * np.sin(2 * np.pi * (t % 1440) / 1440)       # componente diaria
    weekly = 2 * np.sin(2 * np.pi * (t % 10080) / 10080)        # componente semanal
    trend = 0.0002 * t                                          # tendencia suave
    base = daily + weekly + trend

    # montos (heavy-tailed)
    amounts = np.random.lognormal(mean=3.2, sigma=1.0, size=n)
    # promociones esporádicas -> picos
    promo = (np.random.rand(n) < 0.001).astype(float) * np.random.uniform(50,200,size=n)
    price = amounts + promo

    user = np.random.randint(1, 50000, size=n)
    qty = np.random.poisson(1.5, size=n) + 1

    df = pd.DataFrame({
        'timestamp': timestamps,
        'user_id': user,
        'amount': amounts,
        'price': price,
        'quantity': qty,
        'base_demand': base
    })
    # asegurar tipos
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df
