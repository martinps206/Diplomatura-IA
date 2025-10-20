"""Interfaz interactiva con Streamlit para educación e investigación.

Permite cargar valores, ver estadísticas y mostrar el histograma.
"""
import streamlit as st
from typing import List, Optional
from core.statistics_engine import StatisticsEngine
from core.visualizer import plot_histogram, figure_to_png_bytes
from core.utils import validate_values_and_probabilities


def parse_text_to_floats(text: str) -> List[float]:
    return [float(x.strip()) for x in text.split(",") if x.strip()]


def main():
    st.title("Calculadora de Esperanza y Varianza — Interactivo")
    st.write("Introduce una lista de valores separada por comas (ej: 1,2,3,4)")
    txt = st.text_area("Valores", "1,2,3,4,5")
    probs_txt = st.text_area("Probabilidades (opcional)", "")
    if st.button("Calcular"):
        try:
            values = parse_text_to_floats(txt)
            probs = parse_text_to_floats(probs_txt) if probs_txt.strip() else None
            validate_values_and_probabilities(values, probs)
            E = StatisticsEngine.esperanza(values, probs)
            V = StatisticsEngine.varianza(values, probs)
            st.metric("Esperanza (E[X])", f"{E:.4f}")
            st.metric("Varianza (Var[X])", f"{V:.4f}")
            fig = plot_histogram(values, probs, bins=10)
            img = figure_to_png_bytes(fig)
            st.image(img, use_column_width=True)
        except Exception as e:
            st.error(str(e))


if __name__ == "__main__":
    main()
