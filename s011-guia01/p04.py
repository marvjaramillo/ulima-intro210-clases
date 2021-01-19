'''
Entrada: subtotal, porc_gratuidad
Salida: gratuidad, total (mostrar)
'''
subtotal = float(input("Ingrese subtotal: "))
porc_gratuidad = float(input("Ingrese porcentaje gratuidad: "))

gratuidad = subtotal * porc_gratuidad / 100
total = subtotal + gratuidad

print("La gratuidad es:", gratuidad)
print("El monto total es:", total)