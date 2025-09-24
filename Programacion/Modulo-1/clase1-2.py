def ejercicio_1():
    calificaciones = []
    for i in range(3):
        nota = float(input(f"Ingrese la calificación {i+1} (0-10): "))
        calificaciones.append(nota)
    promedio = sum(calificaciones) / 3
    estado = "Aprobado" if promedio >= 6 else "Reprobado"
    print(f"Promedio: {promedio:.2f} - Estado: {estado}")

def ejercicio_2():
    opcion = input("Convertir de (C)elsius a Fahrenheit o de (F)ahrenheit a Celsius? ").upper()
    temp = float(input("Ingrese la temperatura: "))
    if opcion == 'C':
        resultado = (temp * 9/5) + 32
        print(f"{temp}°C = {resultado:.2f}°F")
    elif opcion == 'F':
        resultado = (temp - 32) * 5/9
        print(f"{temp}°F = {resultado:.2f}°C")
    else:
        print("Opción inválida.")

def ejercicio_3():
    num = int(input("Ingrese un número entero: "))
    if num > 0:
        signo = "positivo"
    elif num < 0:
        signo = "negativo"
    else:
        signo = "cero"
    paridad = "par" if num != 0 and num % 2 == 0 else "impar" if num != 0 else "n/a"
    print(f"El número es {signo} y {paridad}.")

def ejercicio_4():
    total_longitud = 0
    cantidad = 0
    for _ in range(100): 
        palabra = input("Ingrese una palabra (vacía para terminar): ")
        if palabra == "":
            break
        longitud = len(palabra)
        total_longitud += longitud
        cantidad += 1
        print(f"Longitud: {longitud}")
    if cantidad > 0:
        promedio = total_longitud / cantidad
        print(f"Promedio de longitudes: {promedio:.2f}")
    else:
        print("No se ingresaron palabras.")

def ejercicio_5():
    monto = float(input("Ingrese el monto de compra: $"))
    if monto < 1000:
        descuento = 0
    elif monto <= 5000:
        descuento = 0.10
    else:
        descuento = 0.20
    precio_final = monto * (1 - descuento)
    print(f"Descuento aplicado: {descuento*100:.0f}% - Precio final: ${precio_final:.2f}")

def ejercicio_6():
    año = int(input("Ingrese un año: "))
    bisiesto = (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)
    print(f"El año {año} {'es' if bisiesto else 'no es'} bisiesto.")

def ejercicio_7():
    numeros = []
    for _ in range(100):  # Límite arbitrario
        num = int(input("Ingrese un número (0 para terminar): "))
        if num == 0:
            break
        numeros.append(num)
    numeros.sort(reverse=True)
    print("Números ordenados de mayor a menor:")
    print(numeros)

# Menú principal
for _ in range(100):  # Puedes ajustar el número de iteraciones
    print("\nSeleccione el número del ejercicio a ejecutar (1-7), o 0 para salir:")
    opcion = int(input("Opción: "))
    if opcion == 0:
        print("Programa finalizado.")
        break
    elif opcion == 1:
        ejercicio_1()
    elif opcion == 2:
        ejercicio_2()
    elif opcion == 3:
        ejercicio_3()
    elif opcion == 4:
        ejercicio_4()
    elif opcion == 5:
        ejercicio_5()
    elif opcion == 6:
        ejercicio_6()
    elif opcion == 7:
        ejercicio_7()
    else:
        print("Opción inválida.")
