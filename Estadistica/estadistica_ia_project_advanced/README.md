# 📊 Proyecto Avanzado de Métodos Estadísticos Aplicados a Inteligencia Artificial  
**Autor:** Martin  
**Versión:** 1.0  
**Lenguaje:** Python 3.10+  
**Dependencias principales:** NumPy, Pandas, SciPy, Matplotlib, Scikit-learn  

---

## 🧠 Descripción General del Proyecto

Este proyecto es una **implementación avanzada en Python** que integra los **métodos estadísticos fundamentales y sus extensiones matemáticas** en el contexto de la **Inteligencia Artificial (IA)**.  

Cada módulo representa un **tema teórico desarrollado en las clases de “Métodos Estadísticos para IA”**, pero expresado de forma **computacional, matemática y aplicada a problemas del mundo real** con grandes volúmenes de datos.  

La arquitectura del proyecto está diseñada para servir como **laboratorio de investigación estadística avanzada**, combinando:
- Análisis descriptivo de grandes datasets  
- Métodos numéricos y álgebra lineal avanzada  
- Visualización de datos y estructuras multidimensionales  
- Técnicas de reducción de dimensionalidad (PCA, SVD aleatorizada, etc.)  
- Implementaciones reproducibles para docencia e investigación  

---

## 🧩 Estructura del Proyecto

🔍 Descripción de los Módulos
data_loader.py

Genera datasets sintéticos de gran tamaño con patrones realistas (estacionales, aleatorios, con ruido, y tendencias).
Ejemplo de aplicación: simulación de comportamiento de usuarios en e-commerce o series de demanda.

Incluye:

Series temporales con estacionalidad y tendencia
Variables cuantitativas y categóricas
Datos con distribuciones log-normales y Poisson

Detección de picos (eventos tipo “promoción”)

📈 Ejemplo de uso:

from src.data_loader import generate_large_synthetic
df = generate_large_synthetic(n=20000)
print(df.head())

visuals.py

Módulo de visualización estadística avanzada con Matplotlib.
Permite generar y guardar automáticamente gráficos en la carpeta outputs/.

Funciones principales:

plot_series(x, y, title, ...): gráficos de series temporales
plot_hist(data, title, bins=100, ...): histogramas de distribución
plot_scatter(x, y, title, ...): gráficos de dispersión

📊 Ejemplo de uso:

from src.visuals import plot_hist
import numpy as np

data = np.random.normal(0, 1, 10000)
plot_hist(data, "Distribución Normal Simulada", bins=50)

advanced/randomized_svd.py

Implementación numérica y matemática del SVD aleatorizado, una técnica eficiente para descomponer matrices grandes en componentes principales.
Usa proyecciones aleatorias y álgebra lineal avanzada para aproximar la descomposición singular.

📘 Aplicaciones:

Reducción de dimensionalidad para IA
Análisis de grandes matrices de datos (Big Data)
Recomendadores, visión por computadora, NLP
advanced/pca_compare.py
Comparación práctica entre:
PCA exacta (utilizando scikit-learn)
PCA aproximada (basada en randomized_svd)

Permite visualizar la diferencia en proyecciones y varianza explicada entre métodos.
Incluye análisis de rendimiento para datasets de alta dimensionalidad.

📊 Ejemplo de uso:

from src.advanced.pca_compare import compare_pca
import numpy as np

X = np.random.randn(5000, 300)
scores_full, scores_rand, var_exp = compare_pca(X, k=5)
print("Varianza explicada:", var_exp)

🧮 Fundamentos Matemáticos

El proyecto integra conceptos avanzados de:
Álgebra Lineal: Descomposición SVD, PCA, Eigenvalores, Proyecciones
Estadística Descriptiva: Medidas de posición, dispersión, normalidad
Cálculo y Análisis Numérico: Optimización y aproximación estocástica
Teoría de la Probabilidad: Modelado de ruido, generación aleatoria y simulaciones
Computación Científica: Manipulación de grandes matrices, eficiencia O(n·p·k)

📂 Resultados y Visualizaciones

Las ejecuciones generan automáticamente gráficos en la carpeta /outputs/, incluyendo:

Histogramas normalizados
Series temporales simuladas
Comparaciones PCA/SVD
Diagramas de dispersión multidimensional