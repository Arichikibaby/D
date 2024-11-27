# Solicitar dos números y la operación
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación (+, -, *, /): ")

# Realizar el cálculo según la operación
if operacion == "+":
    resultado = numero1 + numero2
elif operacion == "-":
    resultado = numero1 - numero2
elif operacion == "*":
    resultado = numero1 * numero2
elif operacion == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Error: División por cero."
else:
    resultado = "Operación no válida."

# Mostrar el resultado
print(f"Resultado: {resultado}")
