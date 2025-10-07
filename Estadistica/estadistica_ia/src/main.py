from src.data_loader import generate_synthetic_ecommerce
from src.visuals import hist_plot, ecdf_plot, qq_plot, boxplot_by
from src.frequencies import frequency_table
from src.measures import sample_mean, sample_std, iqr
from src.feature_engineering import time_features, price_per_item
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA_DIR = BASE / 'data'
OUTPUT_DIR = BASE / 'outputs'
DATA_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

def run_demo(n=20000):
    print('Generando dataset sintético...')
    df = generate_synthetic_ecommerce(n=n)
    df.to_csv(DATA_DIR / 'synthetic_ecommerce.csv', index=False)
    print('Aplicando feature engineering...')
    df = time_features(df)
    df = price_per_item(df)
    print('Calculando medidas...')
    print('Media de price:', sample_mean(df['price']))
    print('Std price:', sample_std(df['price']))
    print('IQR session_time:', iqr(df['session_time_s']))
    print('Creando tablas de frecuencia (price bins)')
    freq = frequency_table(df['price'], bins=30)
    freq.to_csv(OUTPUT_DIR / 'price_frequency_table.csv', index=False)
    print('Generando gráficos (histograma, ecdf, qqplot)')
    hist_path = hist_plot(df['price'], bins=50, filename='price_hist.png', density=True)
    ecdf_path = ecdf_plot(df['price'], filename='price_ecdf.png')
    qq_path = qq_plot(df['price'], filename='price_qq.png')
    box_path = boxplot_by(df['price'], df['quantity'], filename='price_by_qty_box.png')
    print('Gráficos guardados en outputs:')
    print(hist_path)
    print(ecdf_path)
    print(qq_path)
    print(box_path)

if __name__ == '__main__':
    run_demo(n=20000)
