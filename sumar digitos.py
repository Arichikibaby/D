# Solicitar un número entero
numero = int(input("Introduce un número entero: "))

# Inicializar la suma de los dígitos
suma_digitos = 0

# Recorrer cada dígito del número y sumarlo
for digito in str(abs(numero)):  # Usar abs para manejar números negativos
    suma_digitos += int(digito)

# Mostrar el resultado
print(f"La suma de los dígitos es {suma_digitos}.")
