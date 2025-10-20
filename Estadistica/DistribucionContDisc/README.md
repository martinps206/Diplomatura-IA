# AI Probability Lab

Repositorio: DistribucionContDisc

Descripción
-----------
AI Probability Lab es una pequeña aplicación CLI en Python diseñada para explorar distribuciones de probabilidad discretas y continuas. Permite: calcular y mostrar la esperanza (E[X]) y la varianza (Var[X]), mostrar explicaciones didácticas sobre los conceptos y graficar PMF/PDF de varias distribuciones.

Estructura del proyecto
-----------------------
- `main.py` — Punto de entrada CLI. Muestra un menú interactivo donde el usuario elige una distribución, ingresa parámetros y recibe resultados, explicaciones y gráficos.

- `core/` — Lógica central del proyecto.
  - `base_distribution.py` — Clase abstracta base `BaseDistribution` y métodos de compatibilidad `expectation()` y `values()` que generan arrays para graficar.
  - `explanations.py` — Textos y funciones explicativas (p. ej. `explain_expectation`, `explain_variance`) que se usan en la CLI.
  - `continuous/` — Implementaciones de distribuciones continuas:
    - `normal.py` — `NormalDistribution` (mu, sigma)
    - `uniform.py` — `UniformDistribution` (a, b)
    - `chi_square.py` — `ChiSquareDistribution` (k)
    - `student_t.py` — `StudentTDistribution` (df)
  - `discrete/` — Implementaciones de distribuciones discretas:
    - `binomial.py` — `BinomialDistribution` (n, p)
    - `poisson.py` — `PoissonDistribution` (lam / lmbda)
    - `geometric.py` — `GeometricDistribution` (p)
  - `utils/` — Utilidades del proyecto:
    - `random_seed.py` — Fija semilla para reproducibilidad.

- `visualizations/` — Funciones de graficado:
  - `plotter.py` — Clase `DistributionPlotter` y una función de compatibilidad `plot_distribution(x, y, continuous=False, title=None)` usada por la CLI.

- `quick_check.py` — Script de verificación rápida que instancia cada distribución y comprueba `values()`, `expectation()` y `variance()`.

Dependencias
------------
Recomendado instalar las siguientes dependencias en un entorno virtual:

- Python 3.8+ (recomendado)
- numpy
- scipy
- matplotlib

Puedes instalar rápidamente (en PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install numpy scipy matplotlib
```

Ejecución
---------
- Ejecutar la CLI interactiva:

```powershell
python -u main.py
```

Sigue el menú y proporciona los parámetros solicitados. La aplicación imprimirá E[X] y Var[X], mostrará explicaciones y abrirá una ventana con la gráfica correspondiente.

- Ejecutar la comprobación automatizada (sin interacción):

```powershell
python -u quick_check.py
```

Esto imprimirá información resumida de cada distribución y sirve para validar que la API de las distribuciones funciona.

Diseño y contratos (resumen)
---------------------------
- Inputs/Outputs clave:
  - `BaseDistribution.values()` -> (x: np.array, y: np.array) para graficar
  - `BaseDistribution.expectation()` -> float (E[X])
  - `BaseDistribution.variance()` -> float (Var[X])
  - `plot_distribution(x,y, continuous=False, title=None)` -> muestra la gráfica

- Modos de error relevantes:
  - Si faltan dependencias (p.ej. SciPy), algunas funciones pueden fallar al importar; en ese caso instala las dependencias indicadas arriba o solicita que implemente un fallback sin SciPy.

Notas de desarrollo y recomendaciones
------------------------------------
- Para entornos sin SciPy puedo implementar fórmulas cerradas (binomial, poisson, geom) usando `numpy` como fallback. Indica si quieres que lo haga.
- Añadir `requirements.txt` para fijar dependencias y `pytest` para pruebas automatizadas es recomendable si el proyecto crecerá.

Contacto
--------
Si quieres que agregue `requirements.txt`, tests automatizados o implementaciones sin SciPy, dime y lo preparo.
