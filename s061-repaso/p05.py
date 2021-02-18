'''
Tomando en cuenta los supuestos vistos en clase para el analisis de algoritmos,
determine la duracion que tendra el siguiente bloque de codigo en el mejor caso
y en el peor caso.
Finalmente, especifique la complejidad del algoritmo utilizando notacion Big-O.
'''

#n es el tamano de la lista
def procesar_lista(lista, n):
    suma = 0
    for i in range(len(lista)):
        suma = suma + i
        if(n % 2 == 0):
            break        
    print("La suma es:", suma)