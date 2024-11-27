
# Definir la función que calcula el cuadrado de un número
def cuadrado(numero):
    return numero ** 2

# Solicitar un número al usuario
numero_usuario = float(input("Introduce un número: "))

# Llamar a la función y mostrar el resultado
resultado = cuadrado(numero_usuario)
print(f"El cuadrado de {numero_usuario} es: {resultado}")
