"""API REST mínima usando FastAPI para exponer cálculos y gráficos.

Endpoints:
- GET /stats?values=1,2,3&probabilities=0.2,0.3,0.5 -> JSON con esperanza y varianza
- GET /plot.png?values=1,2,3 -> devuelve PNG del histograma
"""
from fastapi import FastAPI, Query, HTTPException, Response
from typing import List, Optional
from core.statistics_engine import StatisticsEngine
from core.utils import validate_values_and_probabilities
from core.explanations import explain_concept
import logging

logger = logging.getLogger("esperanza_varianza_api")


def _get_visualizer():
    # Importar visualizador de forma perezosa para evitar cargar matplotlib en import time
    from core.visualizer import plot_histogram, figure_to_png_bytes
    return plot_histogram, figure_to_png_bytes

app = FastAPI(title="Esperanza-Varianza API")


def _parse_float_list(param: Optional[str]) -> Optional[List[float]]:
    if param is None:
        return None
    try:
        return [float(x) for x in param.split(",") if x != ""]
    except ValueError:
        raise HTTPException(status_code=400, detail="Parámetros numéricos inválidos.")


@app.get("/stats")
def get_stats(values: str = Query(..., description="Lista separada por comas"),
              probabilities: Optional[str] = Query(None, description="Probabilidades separadas por comas")):
    vals = _parse_float_list(values)
    probs = _parse_float_list(probabilities)
    validate_values_and_probabilities(vals, probs)
    esperanza = StatisticsEngine.esperanza(vals, probs)
    varianza = StatisticsEngine.varianza(vals, probs)
    return {"esperanza": esperanza, "varianza": varianza}


@app.get("/plot.png")
def get_plot_png(values: str = Query(..., description="Lista separada por comas"),
                 probabilities: Optional[str] = Query(None, description="Probabilidades separadas por comas"),
                 bins: int = Query(10, ge=1)):
    vals = _parse_float_list(values)
    probs = _parse_float_list(probabilities)
    validate_values_and_probabilities(vals, probs)
    plot_histogram, figure_to_png_bytes = _get_visualizer()
    fig = plot_histogram(vals, probs, bins=bins)
    img = figure_to_png_bytes(fig)
    return Response(content=img, media_type="image/png")


@app.post("/stats")
def post_stats(payload: dict):
    """Recibe JSON: {"values": [...], "probabilities": [...]}

    Devuelve esperanza y varianza.
    """
    try:
        values = payload.get("values")
        probabilities = payload.get("probabilities") if payload else None
        if values is None:
            raise HTTPException(status_code=400, detail="Campo 'values' requerido en el JSON.")
        validate_values_and_probabilities(values, probabilities)
        E = StatisticsEngine.esperanza(values, probabilities)
        V = StatisticsEngine.varianza(values, probabilities)
        return {"esperanza": E, "varianza": V}
    except HTTPException:
        raise
    except Exception as e:
        logger.exception("Error en POST /stats")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/explain")
def explain():
    return {"explanation": explain_concept()}
