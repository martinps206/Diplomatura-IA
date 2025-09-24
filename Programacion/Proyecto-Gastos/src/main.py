"""Entry point: carga datos, corre análisis, genera gráficos y guarda reportes."""
from __future__ import annotations


import argparse
import json
import os
from pathlib import Path


from analisis import (
    load_data,
    clean_data,
    compute_summary,
    moving_average_forecast,
)

from graficos import plot_monthly_expenses, plot_category_expenses
from utils import save_summary_csv, save_summary_json




def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analiza y grafica gastos personales desde un CSV"
    )
    parser.add_argument(
        "--input",
        "-i",
        default="data/gastos_sample.csv",
        help="Ruta al CSV de entrada",
    )
    parser.add_argument(
        "--out",
        "-o",
        default="reports",
        help="Directorio de salida para reportes y figuras",
    )
    return parser.parse_args()




def ensure_dirs(base: Path) -> tuple[Path, Path]:
    base.mkdir(parents=True, exist_ok=True)
    figs = base / "figs"
    figs.mkdir(parents=True, exist_ok=True)
    return base, figs




def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    out_dir = Path(args.out)
    out_dir, figs_dir = ensure_dirs(out_dir)

    print(f"Cargando datos desde {input_path}")
    df = load_data(input_path)
    df = clean_data(df)

    print("Calculando resumen estadístico...")
    summary = compute_summary(df)

    # Predicción simple (media móvil)
    prediction = moving_average_forecast(summary["monthly"], window=3)
    summary["prediction_next_month"] = prediction

    print("Guardando reportes...")
    save_summary_csv(summary, out_dir)
    save_summary_json(summary, out_dir / "summary.json")

    print("Generando gráficas...")
    plot_monthly_expenses(summary["monthly"], figs_dir / "monthly.png")
    plot_category_expenses(summary["category_total"].head(10), figs_dir / "categories.png")

    print("Listo. Revisa el directorio de salida:", out_dir)




if __name__ == "__main__":
    main()