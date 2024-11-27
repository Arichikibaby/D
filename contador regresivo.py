# Usar un bucle para imprimir los números del 10 al 1
for i in range(10, 0, -1):
    print(i, end=", " if i > 1 else "")
