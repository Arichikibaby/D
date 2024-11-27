# Solicitar la edad del usuario
edad = int(input("Introduce tu edad: "))

# Clasificar según la edad
if 0 <= edad <= 12:
    print("Eres niño.")
elif 13 <= edad <= 17:
    print("Eres adolescente.")
elif edad >= 18:
    print("Eres adulto.")
else:
    print("Edad no válida.")
