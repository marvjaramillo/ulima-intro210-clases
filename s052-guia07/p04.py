import random
#Creamos la lista en blanco
lista = []
#Debemos generar 100 numeros
for i in range(100):
    #Generamos numeros aleatorios entre 1 y 1000
    valor = random.randint(1, 1000)
    #Agregar el valor generado a la lista
    lista.append(valor)

#Calculamos el promedio de elementos. Para ello requerimos la suma
suma = 0

#Para ello, recorremos la lista
for i in range(len(lista)): 
    #Por cada elemento, agregamos al total
    suma = suma + lista[i]
#Promedio = suma / cantidad elementos
promedio = suma / len(lista)
print("Lista  generada:", lista)
print("Promedio:", promedio)

#Calculamos cantidad de elementos mayores y menores que el promedio
menores = 0
mayores = 0
#Recorrer la lista
for i in range(len(lista)):
    #Leer el elemento
    elemento = lista[i]
    #Comparar con el promedio
    if(elemento < promedio):
        #Si es menor que el promedio, incrementamos contador de menores
        menores = menores + 1
    else:
        #Si es mayor que el promedio, incrementamos contador de mayores
        mayores = mayores + 1

print("Cantidad de elementos menores que el promedio:", menores)
print("Cantidad de elementos mayores o iguales que el promedio:", mayores)
