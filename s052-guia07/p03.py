#Leer 10 valores enteros
n = 10
#Definimos una lista en blanco
lista = []
for i in range(n):
    valor = int(input("Ingrese numero: "))
    #Almacenar en una lista
    lista.append(valor)

print(lista)    
#Revertir la lista
lista.reverse()
#Mostrar elementos
print(lista)