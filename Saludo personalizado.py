# Definir la función que saluda al usuario
def saludar(nombre):
    return f"Hola, {nombre}!"

# Solicitar el nombre al usuario
nombre_usuario = input("Introduce tu nombre: ")

# Llamar a la función y mostrar el saludo
saludo = saludar(nombre_usuario)
print(saludo)
