# Función para verificar si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Imprimir todos los números primos entre 1 y 50
for num in range(1, 51):
    if es_primo(num):
        print(num, end=", " if num < 50 else "")
