"""Utilidades generales para carga, validación y conversión de datos.

Funciones pequeñas para apoyar al motor estadístico y al visualizador.
"""
from typing import List, Optional

def validate_values_and_probabilities(values: List[float], probabilities: Optional[List[float]] = None):
	"""Valida que las listas sean coherentes y regresan copias.

	Lanza ValueError si hay problemas.
	"""
	if not values:
		raise ValueError("La lista de valores no puede estar vacía.")
	if probabilities is not None:
		if len(values) != len(probabilities):
			raise ValueError("Las listas de valores y probabilidades deben tener la misma longitud.")
		s = sum(probabilities)
		if not abs(s - 1.0) < 1e-6:
			raise ValueError("Las probabilidades deben sumar 1.")
	return list(values), (list(probabilities) if probabilities is not None else None)

