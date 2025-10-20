import pytest
from core.statistics_engine import StatisticsEngine
from core.utils import validate_values_and_probabilities


def test_esperanza_sin_probabilidades():
    vals = [1, 2, 3, 4]
    assert abs(StatisticsEngine.esperanza(vals) - 2.5) < 1e-9


def test_varianza_sin_probabilidades_sample():
    vals = [1, 2, 3, 4]
    # varianza muestral (n-1) -> 1.666666...
    assert pytest.approx(StatisticsEngine.varianza(vals), rel=1e-6) == 1.6666666666666667


def test_esperanza_con_probabilidades():
    vals = [0, 1]
    probs = [0.3, 0.7]
    assert abs(StatisticsEngine.esperanza(vals, probs) - 0.7) < 1e-9


def test_validate_values_and_probabilities_errors():
    with pytest.raises(ValueError):
        validate_values_and_probabilities([], None)
    with pytest.raises(ValueError):
        validate_values_and_probabilities([1, 2], [0.5])
    with pytest.raises(ValueError):
        validate_values_and_probabilities([1, 2], [0.2, 0.3])
