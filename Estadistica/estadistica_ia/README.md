# 📊 Proyecto: Métodos Estadísticos Aplicados a la Inteligencia Artificial

## 🧩 Contenido General

### 🔍 Estructura del Proyecto

## ⚙️ Instalación y Ejecución

### 1️⃣ Requisitos
Instalar dependencias del archivo `requirements.txt`:

```bash
pip install -r requirements.txt

El script generará:

Dataset sintético en /data/synthetic_ecommerce.csv
Gráficos estadísticos en /outputs/
Medidas descriptivas y tablas impresas en consola

3️⃣ Visualizar resultados

Los gráficos generados incluyen:

price_hist.png → Histograma de precios
price_ecdf.png → Distribución acumulada empírica
price_qq.png → Q-Q plot para probar normalidad
price_by_qty_box.png → Diagrama de cajas por cantidad vendida


🧠 Descripción Detallada de los Módulos
🗂️ main.py

Punto de entrada del proyecto.
Orquesta todo el flujo:

Carga o genera los datos
Realiza ingeniería de características
Calcula medidas descriptivas
Construye tablas de frecuencias
Genera los gráficos principales
Guarda resultados en /outputs

📦 data_loader.py

Genera un dataset sintético de comercio electrónico para simulación de escenarios reales.
Variables simuladas:

price: precio del producto
quantity: cantidad vendida
session_time: duración de sesión
category: tipo de producto
timestamp: hora del registro

Este módulo puede adaptarse para leer datos desde CSV o bases SQL reales.

🧮 frequencies.py

Implementa tablas de frecuencia:
Frecuencia absoluta (fi)
Frecuencia acumulada (Fi)
Frecuencia relativa (hi)
Frecuencia relativa acumulada (Hi)

📘 Ejemplo aplicado: distribución de precios agrupada en intervalos, útil para detectar sesgos de mercado o rangos de consumo.

📊 measures.py

Calcula las principales medidas de posición y dispersión:
Media, mediana, moda
Cuartiles, percentiles
Varianza, desviación estándar, IQR
Coeficiente de variación (CV)

📘 Ejemplo aplicado: comparación del precio medio frente al rango intercuartílico para detectar productos con alta variabilidad.

🧱 transformations.py

Aplica transformaciones matemáticas para normalizar o escalar los datos:

Logarítmica (log1p)
Box–Cox
Estandarización (z-score)

📘 Ejemplo aplicado: corrección de sesgos en datos de ingresos antes de aplicar modelos predictivos.

⚙️ feature_engineering.py

Crea nuevas variables útiles para análisis o modelado:
Día y hora desde timestamp
Precio promedio por ítem (price_per_item)
Clasificación de categoría

📘 Ejemplo aplicado: derivar el comportamiento de compra según la hora o el día de la semana.

🧠 advanced_math.py

Contiene métodos matemáticos avanzados relacionados con IA:


📘 Ejemplo aplicado: estimación de probabilidad de gasto por cliente en campañas publicitarias.

📉 visuals.py

Genera visualizaciones estadísticas con matplotlib:
Histogramas normalizados (stat='density')
ECDF (función de distribución acumulada empírica)
Q–Q plots (normalidad)
Diagramas de caja y bigotes (detección de outliers)

📘 Ejemplo aplicado: visualizar la dispersión de precios por categoría o cantidad vendida.

🤖 modeling.py

Integra una demo básica de modelado predictivo (clasificación/regresión) con scikit-learn:

Preparación del dataset
División entrenamiento/prueba
Entrenamiento de modelo
Evaluación de desempeño

📘 Ejemplo aplicado: predicción de compras futuras basadas en el historial del cliente.

🧰 utils.py

Funciones de soporte:
Creación de carpetas
Guardado de archivos
Logging y control de errores

🧪 Temas Estadísticos Aplicados
Tema	Descripción	Implementación
Estadística Descriptiva	Resumen numérico y gráfico de datos	measures.py, visuals.py
Tablas de Frecuencia	Organización de datos en intervalos	frequencies.py
Medidas de Posición	Media, mediana, moda, cuartiles	measures.py
Medidas de Dispersión	Rango, varianza, desviación estándar, CV	measures.py
Transformaciones de Datos	Normalización, Box–Cox, z-score	transformations.py
Visualización	Histogramas, ECDF, QQ-plots, Boxplots	visuals.py
Análisis Avanzado	PCA, KDE	advanced_math.py
Modelado Predictivo	Clasificación y regresión	modeling.py
📚 Ejemplo Real de Aplicación

Escenario: Una empresa de e-commerce desea analizar el comportamiento de precios y consumo de usuarios.

Se generan o cargan registros de ventas (data_loader.py)
Se crean nuevas variables (feature_engineering.py)
Se obtienen medidas de tendencia y dispersión (measures.py)
Se construyen gráficos (visuals.py)
Se detectan sesgos o outliers (boxplot, qqplot)
Se aplica reducción de dimensionalidad (advanced_math.py)
Se entrena un modelo predictivo (modeling.py)
El resultado es un pipeline completo de análisis de datos y comprensión estadística aplicada a IA.