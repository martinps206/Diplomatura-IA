"""
ai_probability_lab/main.py
==================================
CLI principal para el laboratorio de probabilidad e inteligencia artificial.

Proporciona herramientas para el cálculo y la visualización de Esperanza y Varianza
en distintas distribuciones discretas y continuas, con explicaciones teóricas
y representación gráfica.
"""

import sys
from core.discrete.binomial import BinomialDistribution
from core.discrete.poisson import PoissonDistribution
from core.continuous.normal import NormalDistribution
from core.continuous.uniform import UniformDistribution
from core.utils.random_seed import set_random_seed
from core.explanations import explain_expectation, explain_variance
from visualizations.plotter import plot_distribution


def show_menu():
    print("\n========== AI Probability Lab ==========")
    print("Seleccione una distribución para analizar:\n")
    print("Discretas:")
    print("  1. Binomial")
    print("  2. Poisson")
    print("\nContinuas:")
    print("  3. Normal")
    print("  4. Uniforme")
    print("  5. Geométrica")
    print("  6. Chi-cuadrado")
    print("  7. Student-t")
    print("\n  0. Salir")
    return input("\nIngrese su elección: ").strip()


def run_binomial():
    print("\n🧮 Distribución Binomial")
    n = int(input("Ingrese el número de ensayos (n): "))
    p = float(input("Ingrese la probabilidad de éxito (p): "))

    dist = BinomialDistribution(n=n, p=p)
    x, pmf = dist.values()
    mean = dist.expectation()
    var = dist.variance()

    print(f"\nE[X] = {mean:.4f}")
    print(f"Var[X] = {var:.4f}")
    explain_expectation(mean)
    explain_variance(var)
    plot_distribution(x, pmf, title=f"Distribución Binomial (n={n}, p={p})")


def run_poisson():
    print("\n📊 Distribución Poisson")
    λ = float(input("Ingrese el parámetro λ (tasa media de éxito): "))

    dist = PoissonDistribution(lmbda=λ)
    x, pmf = dist.values()
    mean = dist.expectation()
    var = dist.variance()

    print(f"\nE[X] = {mean:.4f}")
    print(f"Var[X] = {var:.4f}")
    explain_expectation(mean)
    explain_variance(var)
    plot_distribution(x, pmf, title=f"Distribución Poisson (λ={λ})")


def run_normal():
    print("\n📈 Distribución Normal")
    mu = float(input("Ingrese la media (μ): "))
    sigma = float(input("Ingrese la desviación estándar (σ): "))

    dist = NormalDistribution(mu=mu, sigma=sigma)
    x, pdf = dist.values()
    mean = dist.expectation()
    var = dist.variance()

    print(f"\nE[X] = {mean:.4f}")
    print(f"Var[X] = {var:.4f}")
    explain_expectation(mean)
    explain_variance(var)
    plot_distribution(x, pdf, continuous=True, title=f"Distribución Normal (μ={mu}, σ={sigma})")


def run_uniform():
    print("\n📏 Distribución Uniforme")
    a = float(input("Ingrese el límite inferior (a): "))
    b = float(input("Ingrese el límite superior (b): "))

    dist = UniformDistribution(a=a, b=b)
    x, pdf = dist.values()
    mean = dist.expectation()
    var = dist.variance()

    print(f"\nE[X] = {mean:.4f}")
    print(f"Var[X] = {var:.4f}")
    explain_expectation(mean)
    explain_variance(var)
    plot_distribution(x, pdf, continuous=True, title=f"Distribución Uniforme ({a}, {b})")


def run_geometric():
    print("\n🎲 Distribución Geométrica")
    p = float(input("Ingrese la probabilidad de éxito (p): "))

    from core.discrete.geometric import GeometricDistribution

    dist = GeometricDistribution(p=p)
    x, pmf = dist.values()
    mean = dist.expectation()
    var = dist.variance()

    print(f"\nE[X] = {mean:.4f}")
    print(f"Var[X] = {var:.4f}")
    explain_expectation(mean)
    explain_variance(var)
    plot_distribution(x, pmf, title=f"Distribución Geométrica (p={p})")


def run_chi_square():
    print("\n📐 Distribución Chi-cuadrado")
    k = int(input("Ingrese los grados de libertad (k): "))

    from core.continuous.chi_square import ChiSquareDistribution

    dist = ChiSquareDistribution(k=k)
    x, pdf = dist.values()
    mean = dist.expectation()
    var = dist.variance()

    mean_text = "No definido" if mean is None else f"{mean:.4f}"

    print(f"\nE[X] = {mean_text}")
    print(f"Var[X] = {var:.4f}")
    explain_expectation(mean if mean is not None else 0)
    explain_variance(var)
    plot_distribution(x, pdf, continuous=True, title=f"Distribución Chi-cuadrado (k={k})")


def run_student_t():
    print("\n📏 Distribución Student-t")
    df = int(input("Ingrese los grados de libertad (df): "))

    from core.continuous.student_t import StudentTDistribution

    dist = StudentTDistribution(df=df)
    x, pdf = dist.values()
    mean = dist.expectation()
    var = dist.variance()

    mean_text = "No definido" if mean is None else f"{mean:.4f}"
    var_text = "Infinito" if var == float('inf') else f"{var:.4f}"

    print(f"\nE[X] = {mean_text}")
    print(f"Var[X] = {var_text}")
    explain_expectation(mean if mean is not None else 0)
    explain_variance(var if var != float('inf') else 0)
    plot_distribution(x, pdf, continuous=True, title=f"Distribución Student-t (df={df})")


def main():
    set_random_seed(42)  # reproducibilidad garantizada
    while True:
        choice = show_menu()
        if choice == "0":
            print("\n👋 Saliendo del AI Probability Lab. ¡Hasta pronto!\n")
            sys.exit(0)
        elif choice == "1":
            run_binomial()
        elif choice == "2":
            run_poisson()
        elif choice == "3":
            run_normal()
        elif choice == "4":
            run_uniform()
        elif choice == "5":
            run_geometric()
        elif choice == "6":
            run_chi_square()
        elif choice == "7":
            run_student_t()
        else:
            print("❌ Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
