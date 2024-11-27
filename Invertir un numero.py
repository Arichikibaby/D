# Solicitar un número entero
numero = int(input("Introduce un número entero: "))

# Invertir el número convirtiéndolo en cadena y luego en entero
numero_invertido = int(str(abs(numero))[::-1])  # Usar abs para manejar números negativos

# Si el número era negativo, agregar el signo negativo
if numero < 0:
    numero_invertido = -numero_invertido

# Mostrar el resultado
print(f"La versión invertida del número es {numero_invertido}.")
