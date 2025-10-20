"""Script de demostración: llama a la API internamente con TestClient,
guarda imágenes en demo_outputs/ y muestra resultados por consola.
"""
import os
import sys
from pathlib import Path

# Asegurar que la raíz del proyecto está en sys.path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from fastapi.testclient import TestClient
from api import app


OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "demo_outputs")
OUT_DIR = os.path.abspath(OUT_DIR)
os.makedirs(OUT_DIR, exist_ok=True)

client = TestClient(app)


def save_plot(params, filename):
    r = client.get("/plot.png", params=params)
    if r.status_code == 200:
        path = os.path.join(OUT_DIR, filename)
        with open(path, "wb") as f:
            f.write(r.content)
        print(f"Guardado plot: {path} ({len(r.content)} bytes)")
    else:
        print(f"Error al generar plot: {r.status_code} - {r.text}")


def demo():
    cases = [
        {"values": "1,2,3,4"},
        {"values": "10,20,30,40,50"},
        {"values": "1,1,2,3,5,8,13,21"},
    ]

    print("== DEMO: GET /stats ==")
    for i, params in enumerate(cases, start=1):
        r = client.get("/stats", params=params)
        print(f"case {i}: params={params} -> status={r.status_code} body={r.json()}")

    print("\n== DEMO: POST /stats ==")
    payload = {"values": [2, 4, 6, 8, 10]}
    r = client.post("/stats", json=payload)
    print(f"POST payload={payload} -> status={r.status_code} body={r.json()}")

    print("\n== DEMO: /explain ==")
    r = client.get("/explain")
    print(r.json().get("explanation", "(no explanation returned)"))

    print("\n== DEMO: Generar plots ==")
    save_plot({"values": "1,2,3,4"}, "plot_case1.png")
    save_plot({"values": "10,20,30,40,50", "bins": 8}, "plot_case2.png")
    save_plot({"values": "1,1,2,3,5,8,13,21", "bins": 6}, "plot_case3.png")


if __name__ == "__main__":
    demo()
