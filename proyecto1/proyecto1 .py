#1.solicita al usuario su nombre y su año de nacimiento

nombre = input("Ingrese su nombre: ")
año_nacimiento = int(input("Ingrese su año de nacimiento: "))
edad = 2025 - año_nacimiento
print(f"Hola {nombre}, tienes aproximadamente {edad} años.")
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")


