# Solicitar un número al usuario
numero = int(input("Introduce un número: "))

# Inicializar el factorial como 1
factorial = 1

# Calcular el factorial usando un bucle
for i in range(1, numero + 1):
    factorial *= i

# Mostrar el resultado
print(f"El factorial de {numero} es {factorial}.")
