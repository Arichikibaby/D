# Solicitar el monto gastado por el cliente
monto = float(input("Introduce el monto gastado: $"))

# Calcular el monto final con o sin descuento
if monto > 100:
    monto_final = monto * 0.8  # Aplicar un descuento del 20%
    print(f"Monto final: ${monto_final:.2f}")
else:
    print(f"Monto final: ${monto:.2f}")
