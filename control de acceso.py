# Definir el usuario y contraseña correctos
usuario_correcto = "admin"
contraseña_correcta = "1234"

# Intentos restantes
intentos = 3

# Bucle para permitir 3 intentos
while intentos > 0:
    # Solicitar nombre de usuario y contraseña
    usuario = input("Introduce tu nombre de usuario: ")
    contraseña = input("Introduce tu contraseña: ")
    
    # Validar si ambos son correctos
    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        print(f"Bienvenido, {usuario}.")
        break  # Salir del bucle si el acceso es correcto
    else:
        intentos -= 1
        if intentos > 0:
            print(f"Acceso denegado. Te quedan {intentos} intentos.")
        else:
            print("Acceso bloqueado. Has agotado todos los intentos.")
