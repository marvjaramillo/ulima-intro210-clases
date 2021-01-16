PI = 3.14159
#Leer radio y longitud
radio = float(input("Ingrese radio del cilindro: "))
longitud = float(input("Ingrese longitud del cilindro: "))

#Calcular el area: pi * (radio ^ 2)
area = PI * radio * radio

#Calcular el volumen: area * longitud
volumen = area * longitud

print("El area es:", area)
print("El volumen es:", volumen)
