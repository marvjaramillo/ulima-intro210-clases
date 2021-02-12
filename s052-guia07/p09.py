#Definimos listas de nombres y longitudes (en blanco)
nombres = []
longitudes = []

#Leemos cantidad de nombres
n = int(input("Ingrese cantidad de nombres: "))

#Leemos datos
for i in range(n):
    nombre_ingresado = input("Ingrese nombre : ")
    nombres.append(nombre_ingresado)
    longitudes.append(len(nombre_ingresado))

#Mostrar nombres y longitudes
for i in range(n):
    print("*" * 10)
    print("Nombre:", nombres[i])
    print("Longitud:", longitudes[i])
    print("*" * 10)


