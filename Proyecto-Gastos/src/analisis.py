"""Funciones de carga, limpieza y análisis de datos de gastos."""
from __future__ import annotations

from typing import Dict

import numpy as np
import pandas as pd




def load_data(path: str) -> pd.DataFrame:
	"""Lee un CSV y devuelve un DataFrame. Intenta parsear la columna 'fecha'."""
	df = pd.read_csv(path)
	if "fecha" in df.columns:
		df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
	return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
	"""Limpia y normaliza el DataFrame.

	- Elimina filas con fecha o monto inválidos.
	- Convierte 'monto' a numérico.
	- Normaliza cadenas de categoría.
	- Agrega columna 'year_month' para agrupar por mes.
	"""
	df = df.copy()
	# Normalizar columnas
	if "categoria" in df.columns:
		df["categoria"] = df["categoria"].astype(str).str.strip()
	# Monto a numérico
	if "monto" in df.columns:
		df["monto"] = pd.to_numeric(df["monto"], errors="coerce")
	# Eliminar filas inválidas
	df = df.dropna(subset=[c for c in ["fecha", "monto"] if c in df.columns])
	# Agregar columna mes-año
	df["year_month"] = df["fecha"].dt.to_period("M").astype(str)
	return df

def compute_summary(df: pd.DataFrame) -> Dict[str, object]:
	"""Calcula varias estadísticas y agregaciones.

	Devuelve un diccionario con:
	- total
	- mean, median, var, std
	- category_total (Series)
	- monthly (Series index ordenado por mes)
	"""
	total = df["monto"].sum()
	mean = df["monto"].mean()
	median = df["monto"].median()
	var = df["monto"].var(ddof=0)
	std = df["monto"].std(ddof=0)

	category_total = df.groupby("categoria")["monto"].sum().sort_values(ascending=False)
	monthly = df.groupby("year_month")["monto"].sum().sort_index()

	return {
		"total": float(total),
		"mean": float(mean),
		"median": float(median),
		"var": float(var),
		"std": float(std),
		"category_total": category_total,
		"monthly": monthly,
	}


def moving_average_forecast(series: pd.Series, window: int = 3) -> float:
    """Predice el siguiente valor usando la media móvil de las últimas `window` observaciones."""
    if len(series) == 0:
        return 0.0
    values = series.dropna().values
    if len(values) == 0:
        return 0.0
    w = min(window, len(values))
    return float(np.mean(values[-w:]))
