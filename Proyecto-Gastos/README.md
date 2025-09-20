# Sistema de Análisis y Predicción de Gastos Personales

## 1. Resumen del proyecto

**Objetivo:** Construir una aplicación educativa en Python que lea registros de gastos personales desde un CSV, realice limpieza y agregaciones con `pandas` y `numpy`, genere visualizaciones con `matplotlib` y entregue un pequeño pronóstico basado en media móvil.


**Por qué es relevante:** El control y análisis del gasto es una aplicación directa y cuantificable en la vida diaria. Permite practicar técnicas de manipulación de datos, estadística descriptiva, visualización y un primer acercamiento a series temporales.


## 2. Objetivos de aprendizaje (para la clase)

- Dominar la carga y limpieza de datos con `pandas`.
- Aplicar estadísticas básicas: suma, media, mediana, varianza y desviación estándar.
- Agrupar y agregar datos por categorías y por mes.
- Visualizar series temporales y distribuciones con `matplotlib`.
- Implementar una predicción simple (media móvil) y discutir métricas de evaluación.
- Practicar buenas prácticas de desarrollo: estructura modular, docstrings y control de versiones.


## 3. Características principales

- Lectura de CSV con fechas y montos.
- Normalización de categorías y validación de montos.
- Cálculo de: gasto total, media, mediana, varianza, desviación estándar.
- Agregación: gasto por categoría y gasto mensual.
- Gráficos: serie temporal mensual y barras por categoría.
- Pronóstico simple del próximo mes mediante media móvil.
- Guardado de reportes en `reports/` (CSV, JSON, imágenes).


## 4. Formato de datos de entrada
Archivo CSV con columnas mínimas:


```csv
fecha,categoria,monto
2025-01-03,Alimentación,1200
2025-01-05,Transporte,300


Ejecutar el análisis con el dataset de ejemplo:
python src/main.py --input data/gastos_sample.csv --out reports


Archivos generados en reports/:
summary.json — resumen serializado (estadísticas, agregaciones, predicción).
monthly.csv — gasto total por mes.
category.csv — gasto total por categoría.
summary_stats.json — estadísticas principales.
figs/monthly.png y figs/categories.png — gráficos.


Descripción técnica de los módulos

main.py: 
    Orquesta la ejecución: carga, limpieza, análisis, guardado y graficado.

analisis.py: 
    load_data(path) — lee CSV y convierte fecha.
    clean_data(df) — normaliza categorías, convierte monto a numérico y crea year_month.
    compute_summary(df) — devuelve total, mean, median, var, std, category_total y monthly.
    moving_average_forecast(series, window=3) — predice el siguiente mes usando media móvil.

graficos.py: 
    plot_monthly_expenses(monthly, out_path) — serie temporal.
    plot_category_expenses(category_series, out_path) — barras.

utils.py:
    Guardado de CSV/JSON y serialización de pandas.Series.


Conclusión

Este proyecto integra conceptos de programación, matemáticas aplicadas y análisis de datos para resolver un problema cotidiano: entender cómo se distribuyen y predicen los gastos personales. Es ideal para exposición en clase, ya que combina teoría y práctica de manera clara y demostrativa.