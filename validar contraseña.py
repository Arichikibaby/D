# Definir la contraseña correcta
contraseña_correcta = "12345"

# Solicitar la contraseña al usuario
contraseña = input("Introduce la contraseña: ")

# Validar la contraseña
if contraseña == contraseña_correcta:
    print("Acceso concedido.")
else:
    print("Acceso denegado.")
