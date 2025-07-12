#Escribe un programa que use un bucle while para imprimir números desde el 10 hasta el 1.
numero = 10
while numero >= 1:
    print(numero)
    numero -= 1 
print("despegue")
#Escribe un programa que defina una palabra secreta (por ejemplo, puedes usar "python").
palabra_secreta = "tangamangapio"
while True:
    palabra = input("adivina la palabra secreta: ")
    if palabra == palabra_secreta:
        print("has adivinado la palabra")
        break
    else:
        print("intentalo de nuevo")
#Escribe un programa que pida al usuario que ingrese texto repetidamente usando un bucle while True.
while True:
    texto = input("Escribe algo: ")
    if texto == "#":
        continue
    if texto == "listo":
        print("¡Procesamiento terminado!")
        break
    print(texto)
#Define una lista de nombres de amigos. Por ejemplo: invitados = ['Ana', 'Luis', 'Carla', 'Pedro'].
invitados = ['maria', 'rigoverto', 'atreos', 'cristoval']
for nombre in invitados:
    print("hola", nombre, "bienvenido a la fiesta")
#Se proporciona la siguiente lista de números: numeros = [3, 41, 12, 9, 74, 15, 1, 55].
numeros = [3,41,12,9,74,15,1,55]
mayor_hasta_ahora = -1
for numero in numeros:
    if numero > mayor_hasta_ahora:
        mayor_hasta_ahora = numero
print(mayor_hasta_ahora)
#Se proporciona la siguiente lista de números: numeros = [2, 5, 8, 11, 14, 17, 20, 23].
numeros = [2,5,8,11,14,17,20,23]
contador = 0
for numero in numeros:
    if numero % 2 == 0:
        contador = contador + 1
print(contador)
#Se proporciona la siguiente lista de números: numeros = [10, 20, 30, 40, 50].
numeros = [10,20,30,40,50]
suma_total = 0
for numero in numeros:
    suma_total = suma_total + numero
print(suma_total)
#Se proporciona la siguiente lista de números: numeros = [10, 15, 20, 25, 30].
numeros = [10,15,20,25,30]
suma_total = 0
contador = 0
for numero in numeros:
    suma_total = suma_total + numero
    contador = contador + 1
promedio = suma_total / contador
print(promedio)
#Se proporciona la siguiente lista de números: numeros = [5, 25, 12, 33, 18, 45, 7].
numeros = [5,25,12,33,18,45,7]
umbral = int(input("ingresa un numero umbral: "))
for numero in numeros:
    if numero > umbral:
        print(numero)
#Se proporciona la siguiente lista de números: numeros = [9, 41, 12, 3, 74, 15].
numeros = [9,41,12,3,74,15]
encontrado = False
for numero in numeros:
    if numero == 3:
        encontrado = True
        break
print("el valor 3 fue encontrado:", encontrado)
#Se proporciona la siguiente lista de números: numeros = [30, 10, 5, 25, 50, 2].
numeros = [30,10,5,25,50,2]
menor_hasta_ahora = None
for numero in numeros:
    if menor_hasta_ahora is None:
        menor_hasta_ahora = numero
    elif numero < menor_hasta_ahora:
        menor_hasta_ahora = numero
print(menor_hasta_ahora)