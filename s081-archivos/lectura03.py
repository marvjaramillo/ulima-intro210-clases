archivo = open("data/notas2.txt")
for linea in archivo:
    lista = linea.split(",")
    print(lista)