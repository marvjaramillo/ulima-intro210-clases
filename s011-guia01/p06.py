'''
Entradas: ahorro_mensual, tea
Salida: monto total al finalizar el cuarto mes
'''
ahorro_mensual = float(input("Ingrese monto de ahorro mensual: "))
tea = float(input("Ingrese TEA (ratio): "))

#Convertimos la TEA (anual) a TEM (mensual)
tem = ((1+tea) ** (1/12)) - 1

m1 = ahorro_mensual * (1+tem)
m2 = (ahorro_mensual+m1) * (1+tem)
m3 = (ahorro_mensual+m2) * (1+tem)
m4 = (ahorro_mensual+m3) * (1+tem)

print("Al final del 4to mes se tiene:", m4)