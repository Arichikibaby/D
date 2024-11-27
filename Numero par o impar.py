# Definir la función que verifica si un número es par o impar
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# Solicitar un número al usuario
numero_usuario = int(input("Introduce un número: "))

# Llamar a la función y mostrar el resultado
resultado = es_par(numero_usuario)
print(resultado)
