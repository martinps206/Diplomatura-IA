import argparse
from core.statistics_engine import StatisticsEngine
from core.explanations import explain_concept

def main():
    parser = argparse.ArgumentParser(
        description="Aplicación avanzada para calcular Esperanza y Varianza."
    )
    parser.add_argument(
        "--values", nargs="+", type=float, required=True,
        help="Valores de la variable aleatoria (ej: --values 1 2 3 4)"
    )
    parser.add_argument(
        "--probabilities", nargs="+", type=float,
        help="Probabilidades asociadas (ej: --probabilities 0.1 0.2 0.3 0.4)"
    )
    args = parser.parse_args()

    print("\n=== Calculadora de Esperanza y Varianza ===")
    print(explain_concept())
    print(f"Valores: {args.values}")
    if args.probabilities:
        print(f"Probabilidades: {args.probabilities}")

    esperanza = StatisticsEngine.esperanza(args.values, args.probabilities)
    varianza = StatisticsEngine.varianza(args.values, args.probabilities)

    print("\n📈 Resultados:")
    print(f"Esperanza (E[X]) = {esperanza:.4f}")
    print(f"Varianza (Var[X]) = {varianza:.4f}")

if __name__ == "__main__":
    main()
