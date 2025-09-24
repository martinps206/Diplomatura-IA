"""Utilidades para guardar reportes en CSV/JSON."""
from __future__ import annotations


import json
from pathlib import Path
from typing import Dict


import pandas as pd




def save_summary_csv(summary: Dict[str, object], out_dir: str | Path) -> None:
    out_dir = Path(out_dir)
    # Guardar monthly
    monthly = summary.get("monthly")
    if monthly is not None:
        monthly.to_csv(out_dir / "monthly.csv", header=["monto"]) # index = month
    # Guardar category
    cat = summary.get("category_total")
    if cat is not None:
        cat.to_csv(out_dir / "category.csv", header=["monto"]) # index = categoria
    # Guardar estadisticas generales como csv de una fila
    stats = {k: v for k, v in summary.items() if k in {"total", "mean", "median", "var", "std", "prediction_next_month"}}
    stats_path = out_dir / "summary_stats.json"
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)




def save_summary_json(summary: Dict[str, object], path: str | Path) -> None:
    path = Path(path)
    # Convertir series a dicts
    serializable = {}
    for k, v in summary.items():
        if isinstance(v, pd.Series):
            serializable[k] = v.to_dict()
        else:
            # intentar convertir a tipos base (float, int, str, None)
            try:
                json.dumps({"x": v})
                serializable[k] = v
            except TypeError:
                serializable[k] = str(v)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(serializable, f, ensure_ascii=False, indent=2)