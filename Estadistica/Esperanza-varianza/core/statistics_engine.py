from typing import List, Optional

class StatisticsEngine:
    """Clase central para el cálculo de esperanza y varianza."""

    @staticmethod
    def esperanza(values: List[float], probabilities: Optional[List[float]] = None) -> float:
        """
        Calcula la esperanza matemática (media esperada).
        Args:
            values: lista de valores (x_i)
            probabilities: lista opcional de probabilidades asociadas (p_i)
        Returns:
            float: valor esperado E[X]
        """
        if probabilities:
            if len(values) != len(probabilities):
                raise ValueError("Las listas de valores y probabilidades deben tener la misma longitud.")
            if not abs(sum(probabilities) - 1.0) < 1e-6:
                raise ValueError("Las probabilidades deben sumar 1.")
            return sum(x * p for x, p in zip(values, probabilities))
        else:
            return sum(values) / len(values)

    @staticmethod
    def varianza(values: List[float], probabilities: Optional[List[float]] = None) -> float:
        """
        Calcula la varianza (medida de dispersión).
        Args:
            values: lista de valores
            probabilities: lista opcional de probabilidades asociadas

        Returns:
            float: varianza de la variable
        """
        E = StatisticsEngine.esperanza(values, probabilities)
        if probabilities:
            E2 = sum((x ** 2) * p for x, p in zip(values, probabilities))
            return E2 - E ** 2
        else:
            n = len(values)
            return sum((x - E) ** 2 for x in values) / (n - 1)
