import random

# ========================
# EJERCICIO 1
# ========================
def contar_vocales(palabra: str) -> int:
    """Recibe una palabra y retorna la cantidad de vocales."""
    vocales = "aeiouáéíóú"
    return sum(1 for letra in palabra.lower() if letra in vocales)


# ========================
# EJERCICIO 2
# ========================

# ========================
# EJERCICIO 3
# ========================
def digitos_y_suma(numero: int) -> tuple[int, int]:
    """Retorna la cantidad de dígitos y la suma de los mismos."""
    digitos = [int(d) for d in str(abs(numero))]
    return len(digitos), sum(digitos)


# ========================
# EJERCICIO 4
# ========================
def generar_y_ordenar():
    """Genera 100 números aleatorios y los ordena."""
    numeros = [random.uniform(0, 10) for _ in range(100)]
    numeros.sort()
    return numeros


# ========================
# EJERCICIO 5
# ========================
class Estudiante:
    def __init__(self, nombre: str, apellido: str, nota_final: float):
        self.nombre = nombre
        self.apellido = apellido
        self.nota_final = nota_final

    def nombre_completo(self) -> str:
        return f"{self.nombre} {self.apellido}"

    def estado(self) -> str:
        return "Aprobado" if self.nota_final >= 6 else "Desaprobado"


def prueba_estudiantes():
    estudiantes = [
        Estudiante("Ana", "Pérez", 8),
        Estudiante("Luis", "García", 5),
        Estudiante("Marta", "López", 9),
    ]
    for e in estudiantes:
        print(f"{e.nombre_completo()} - {e.estado()}")


# ========================
# EJERCICIO 6
# ========================
class CuentaBancaria:
    def __init__(self, titular: str, saldo: float = 0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto: float):
        self.saldo += monto
        print(f"Depósito exitoso. Saldo actual: {self.saldo}")

    def retirar(self, monto: float):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro exitoso. Saldo actual: {self.saldo}")
        else:
            print("Fondos insuficientes.")

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}")


def prueba_cuenta():
    cuenta = CuentaBancaria("Carlos", 1000)
    cuenta.mostrar_saldo()
    cuenta.depositar(500)
    cuenta.retirar(300)
    cuenta.retirar(1500)


# ========================
# EJERCICIO 7
# ========================
class EquipoFutbol:
    def __init__(self, nombre: str, ciudad: str, puntos: int = 0):
        self.nombre = nombre
        self.ciudad = ciudad
        self.puntos = puntos

    def mostrar_info(self):
        print(f"Equipo: {self.nombre}, Ciudad: {self.ciudad}, Puntos: {self.puntos}")

    def sumar_puntos(self, resultado: str):
        if resultado == "gana":
            self.puntos += 3
        elif resultado == "empata":
            self.puntos += 1
        elif resultado == "pierde":
            self.puntos += 0
        else:
            print("Resultado no válido")


def prueba_equipos():
    equipo1 = EquipoFutbol("Boca", "Buenos Aires")
    equipo2 = EquipoFutbol("River", "Buenos Aires")
    equipo1.mostrar_info()
    equipo2.mostrar_info()

    print("\nDespués del partido:")
    equipo1.sumar_puntos("gana")
    equipo2.sumar_puntos("pierde")
    equipo1.mostrar_info()
    equipo2.mostrar_info()


# ========================
# EJERCICIO 8
# ========================
class Producto:
    def __init__(self, nombre: str, precio: float, cantidad_disponible: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def mostrar_descripcion(self):
        print(f"Producto: {self.nombre}, Precio: {self.precio}, Stock: {self.cantidad_disponible}")

    def vender(self, cantidad: int):
        if cantidad <= self.cantidad_disponible:
            self.cantidad_disponible -= cantidad
            print(f"Venta exitosa. Stock actual: {self.cantidad_disponible}")
        else:
            print("Error: No hay suficiente stock.")

    def reponer(self, cantidad: int):
        self.cantidad_disponible += cantidad
        print(f"Reposición exitosa. Stock actual: {self.cantidad_disponible}")

    def calcular_valor_total(self):
        return self.precio * self.cantidad_disponible


def prueba_productos():
    p1 = Producto("Laptop", 1200, 5)
    p2 = Producto("Mouse", 20, 50)
    p1.mostrar_descripcion()
    p2.mostrar_descripcion()
    p1.vender(2)
    p2.vender(60)
    p2.reponer(20)
    print(f"Valor total del stock de {p1.nombre}: {p1.calcular_valor_total()}")
    print(f"Valor total del stock de {p2.nombre}: {p2.calcular_valor_total()}")


# ========================
# MENÚ PRINCIPAL
# ========================
def menu():
    while True:
        print("\n=== MENÚ DE EJERCICIOS ===")
        print("1. Contar vocales")
        print("2. Explicar función")
        print("3. Cantidad y suma de dígitos")
        print("4. Generar y ordenar números")
        print("5. Clase Estudiante")
        print("6. Clase CuentaBancaria")
        print("7. Clase EquipoFutbol")
        print("8. Clase Producto")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                palabra = input("Ingrese una palabra: ")
                print("Cantidad de vocales:", contar_vocales(palabra))
            case "2":
                explicar_funcion()
            case "3":
                numero = int(input("Ingrese un número entero: "))
                cant, suma = digitos_y_suma(numero)
                print(f"Dígitos: {cant}, Suma: {suma}")
            case "4":
                numeros = generar_y_ordenar()
                print(numeros)
            case "5":
                prueba_estudiantes()
            case "6":
                prueba_cuenta()
            case "7":
                prueba_equipos()
            case "8":
                prueba_productos()
            case "0":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción inválida. Intente de nuevo.")


# ========================
# PROGRAMA PRINCIPAL
# ========================
if __name__ == "__main__":
    menu()
