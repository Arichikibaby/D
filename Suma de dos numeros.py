# Definir la función que calcula la suma de dos números
def sumar(num1, num2):
    return num1 + num2

# Solicitar dos números al usuario
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

# Llamar a la función y mostrar el resultado
resultado = sumar(numero1, numero2)
print(f"La suma es: {resultado}")
