lista = [10, 23, 344, 231, 400, 1000]
valor_buscado = 700
indice = -1
#Recorrido de lista
for i in range(len(lista)):
    elemento = lista[i]
    if(elemento == valor_buscado):
        indice = i
        break
if(indice == -1):
    print("Elemento no encontrado")
else:
    print("Elemento encontrado en posicion:", indice)
