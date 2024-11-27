# Inicializar variables para la suma de calificaciones y la cantidad de entradas
suma_calificaciones = 0
cantidad_calificaciones = 0

# Solicitar calificaciones al usuario hasta que ingrese -1
while True:
    calificacion = float(input("Introduce una calificación (o -1 para terminar): "))
    
    # Salir del bucle si la calificación es -1
    if calificacion == -1:
        break
    
    # Sumar la calificación y aumentar el contador de entradas
    suma_calificaciones += calificacion
    cantidad_calificaciones += 1

# Calcular y mostrar el promedio
if cantidad_calificaciones > 0:
    promedio = suma_calificaciones / cantidad_calificaciones
    print(f"Promedio: {promedio:.2f}")
else:
    print("No se ingresaron calificaciones.")
