# Calculadora de Esperanza y Varianza

Proyecto educativo para calcular la esperanza matemática y la varianza de un conjunto de números, generar visualizaciones (histogramas + curva de densidad) y exponer la lógica como API REST.

Contenido principal
- `main.py`: CLI simple para calcular esperanza y varianza.
- `api.py`: API REST (FastAPI) con endpoints para cálculo y gráficos.
- `core/statistics_engine.py`: Lógica principal (esperanza y varianza).
- `core/visualizer.py`: Genera histogramas y curvas de densidad (matplotlib + seaborn).
- `core/utils.py`: Validaciones y utilidades.
- `core/explanations.py`: Texto explicativo sobre los conceptos.
- `app_streamlit.py`: Interfaz interactiva con Streamlit (UI educativa).
- `tools/run_demo.py`: Script que usa TestClient para llamar a la API internamente y guardar PNGs de ejemplo en `demo_outputs/`.
- `tests/`: tests unitarios y de API (TestClient).

Requisitos
- Python 3.11 (probado en el entorno local del proyecto).
- Las dependencias están en `requirements.txt`.

Instalación (Windows / PowerShell)

1. Crear y activar un entorno virtual (recomendado):

```pwsh
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instalar dependencias:

```pwsh
python -m pip install -r requirements.txt
```

Notas: si `uvicorn` no se encuentra en PATH, usa `python -m uvicorn` (módulo del intérprete activo).

Ejecutar la API (desarrollo)

En una terminal (desde la raíz del proyecto):

```pwsh
# modo recarga durante desarrollo
python -m uvicorn api:app --reload
```

Endpoints principales

- GET /stats?values=1,2,3,4
  - Devuelve JSON con `esperanza` y `varianza`.
  - Ejemplo (PowerShell):
    ```pwsh
    Invoke-RestMethod -Uri "http://127.0.0.1:8000/stats?values=1,2,3,4"
    ```

- POST /stats
  - Envía JSON: `{"values": [...], "probabilities": [...]}` y obtiene JSON con resultados.
  - Ejemplo (PowerShell):
    ```pwsh
    Invoke-RestMethod -Uri "http://127.0.0.1:8000/stats" -Method POST -Body (ConvertTo-Json @{ values = @(1,2,3,4) }) -ContentType "application/json"
    ```

- GET /plot.png?values=1,2,3,4&bins=10
  - Devuelve un PNG con el histograma y la curva de densidad.
  - Ejemplo para guardar en disco:
    ```pwsh
    Invoke-WebRequest -Uri "http://127.0.0.1:8000/plot.png?values=1,2,3,4" -OutFile plot.png
    ```

- GET /explain
  - Devuelve una explicación textual sobre esperanza y varianza.

Demo local (sin levantar servidor externo)

Se incluye `tools/run_demo.py` que usa `fastapi.testclient.TestClient` para llamar a la API internamente y generar gráficos de ejemplo sin exponer puertos.

```pwsh
python tools\run_demo.py

# Los PNG se guardan en 'demo_outputs/' (relativo al repo)
```

Ejecutar la interfaz Streamlit

```pwsh
streamlit run app_streamlit.py
```

Pruebas

Ejecutar la suite de tests con pytest:

```pwsh
pytest -q
```

Problemas comunes y soluciones

- `uvicorn` no reconocido
  - Usa `python -m uvicorn ...` para arrancar con el intérprete actual.

- Incompatibilidad NumPy / Matplotlib (error similar a "A module that was compiled using NumPy 1.x cannot be run in NumPy 2.x" o "_ARRAY_API not found")
  - Causa: algunas ruedas binarias instaladas fueron compiladas contra NumPy 1.x; si tienes NumPy 2.x puede provocar fallos.
  - Solución probada en este proyecto: instalar NumPy 1.26.x:
    ```pwsh
    python -m pip install "numpy<2"
    ```
  - Nota: esto puede causar conflictos con paquetes que requieran NumPy 2.x (por ejemplo opencv); ajusta según tu entorno.

- `ModuleNotFoundError: No module named 'core'` al ejecutar scripts
  - Ejecuta los scripts desde la raíz del proyecto o añade la raíz al `PYTHONPATH` o en el script inserta el root en `sys.path` (como hacemos en `tools/run_demo.py`).

- Problemas con directorio de configuración de matplotlib (permisos)
  - Puedes forzar `MPLCONFIGDIR` a una carpeta temporal con permisos de escritura:
    ```pwsh
    $env:MPLCONFIGDIR = 'C:\temp\matplotlib'
    python -m uvicorn api:app --reload
    ```

Diseño y consideraciones

- `core/visualizer.py` hace importaciones perezosas de matplotlib y seaborn dentro de las funciones para evitar cargar extensiones pesadas al importar `api.py`.
- La API está pensada para ser simple y educativa: los endpoints aceptan listas pequeñas y devuelven resultados numéricos y gráficos estáticos (PNG).

Contribuir

- Añadir tests para nuevos endpoints o mejoras.
- Mejorar la UI de Streamlit para permitir carga de CSV y selección de columnas.

Resumen rápido de comandos útiles

```pwsh
# crear venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1
# instalar deps
python -m pip install -r requirements.txt
# ejecutar API
python -m uvicorn api:app --reload
# probar endpoint
Invoke-RestMethod -Uri "http://127.0.0.1:8000/stats?values=1,2,3,4"
# ejecutar demo (genera PNGs en demo_outputs)
python tools/run_demo.py
# correr streamlit
streamlit run app_streamlit.py
# tests
pytest -q
```

Si quieres, puedo:
- Añadir un endpoint POST `/plot` que reciba JSON y devuelva el PNG.
- Mejorar `app_streamlit.py` para cargar CSV y explicar automáticamente los resultados.
- Crear un `README` más corto para usuarios finales o un `CHANGELOG`.

— Fin —
