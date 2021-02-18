'''
Las notas de un grupo de estudiantes se encuentra almacenadas en una lista L.
Implemente un programa que reciba esta lista y calcule el promedio del grupo
sin considerar la nota mayor y la nota menor.
'''

def calcular_promedio(L):
    mayor = L[0]
    menor = L[0]
    suma = 0
    for i in range(len(L)):
        nota = L[i]
        suma = suma + nota
        if(nota > mayor):
            mayor = nota
        if(nota < menor):
            menor = nota
    print("Valor mayor:", mayor)
    print("Menor valor:", menor)
    promedio = (suma-mayor-menor) / (len(L)-2)
    return promedio

if __name__ == "__main__":
    lista = [10, 12, 16, 18, 11, 5, 13]
    promedio = calcular_promedio(lista)
    print("Promedio sin considerar mayor ni menor:", promedio)
