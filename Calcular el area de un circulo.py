import math

# Definir la función que calcula el área de un círculo
def area_circulo(radio):
    return math.pi * radio ** 2

# Solicitar el radio al usuario
radio_usuario = float(input("Introduce el radio del círculo: "))

# Llamar a la función y mostrar el resultado
resultado = area_circulo(radio_usuario)
print(f"El área del círculo con radio {radio_usuario} es: {resultado:.2f}")
