"""Generación de gráficos con matplotlib (sin estilos externos)."""
from __future__ import annotations


from pathlib import Path


import matplotlib.pyplot as plt
import pandas as pd




def plot_monthly_expenses(monthly: pd.Series, out_path: str | Path) -> None:
	"""Grafica la serie temporal de gastos mensuales y guarda la figura."""
	out_path = Path(out_path)
	plt.figure(figsize=(8, 4))
	ax = monthly.plot(marker="o")
	ax.set_title("Gasto mensual total")
	ax.set_xlabel("Mes")
	ax.set_ylabel("Monto")
	plt.tight_layout()
	plt.savefig(out_path)
	plt.close()


def plot_category_expenses(category_series: pd.Series, out_path: str | Path) -> None:
	"""Grafica las categorías (barras) — espera una Series indexada por categoría."""
	out_path = Path(out_path)
	plt.figure(figsize=(8, 4))
	ax = category_series.plot(kind="bar")
	ax.set_title("Gasto por categoría")
	ax.set_xlabel("Categoría")
	ax.set_ylabel("Monto")
	plt.xticks(rotation=45, ha="right")
	plt.tight_layout()
	plt.savefig(out_path)
	plt.close()