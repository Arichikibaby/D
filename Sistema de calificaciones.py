# Solicitar la calificación numérica
calificacion = float(input("Introduce tu calificación: "))

# Determinar la letra correspondiente
if 90 <= calificacion <= 100:
    letra = "A"
elif 80 <= calificacion <= 89:
    letra = "B"
elif 70 <= calificacion <= 79:
    letra = "C"
elif 60 <= calificacion <= 69:
    letra = "D"
else:
    letra = "F"

# Mostrar el resultado
print(f"Tu calificación es {letra}.")
