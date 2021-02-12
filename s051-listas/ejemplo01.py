'''
Implemente un programa que permita leer "n" elementos ingresados desde el teclado
y los agregue a una lista. Muestre la lista al final
'''

def leer_valores():
    #Crear una lista en blanco
    res = []
    #Leer el valor de "n"
    n = int(input("Ingrese el valor de n: "))
    #Repetir "n" veces
    for i in range(n):
        #Leer el valor desde el teclado
        valor = int(input("Ingrese siguiente valor: "))
        #Agregarlo a la lista
        res.append(valor)
    #Retornar la lista
    return res

if __name__ == "__main__":
    lista = leer_valores()
    print(lista)