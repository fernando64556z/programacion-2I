#mini proyecto
def adivina_numero():
    print("\nJuego de Adivinar el Número")
    import random
    numero_secreto = random.randint(1, 10)
    intento = 0
    while intento != numero_secreto:
        intento = int(input("Adivina el número (1-10): "))
        if intento < numero_secreto:
            print("¡Muy bajo! Intenta otra vez.")
        elif intento > numero_secreto:
            print("¡Muy alto! Intenta otra vez.")
        else:
            print("¡Correcto! Adivinaste el número.")

def calcular_promedio():
    print("\nCalcula el Promedio de tus Notas")
    notas = []
    cantidad = int(input("¿Cuántas notas quieres ingresar? "))
    for i in range(cantidad):
        nota = float(input("Ingresa la nota: "))
        notas.append(nota)
    promedio = sum(notas) / len(notas)
    print("El promedio de las notas es:", promedio)

def multiplicar():
    print("\nMultiplicación de Dos Números")
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    resultado = a * b
    print("El resultado de la multiplicación es:", resultado)

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Adivina el número")
        print("2. Calcular promedio")
        print("3. Multiplicar dos números")
        print("4. Salir")
        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            adivina_numero()
        elif opcion == "2":
            calcular_promedio()
        elif opcion == "3":
            multiplicar()
        elif opcion == "4":
            print("¡Adiós!")
            break
        else:
            print("Opción inválida. Intenta otra vez.")

menu()