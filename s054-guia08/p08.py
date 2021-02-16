'''
Formato de los datos (ambos son cadenas):
    - clave: termino
    - valor: definicion del termino
    Ejemplo:
    glosario =  {"termino1": "El termino1 es <definicion>"}
'''

#Lee los valores del usuario y crea el diccionario
def leer_glosario():
    res = {}
    #Leemos la cantidad de terminos
    n = int(input("Ingrese la cantidad de terminos: "))
    for i in range(n):
        #Por cada uno, leemos el termino y su definicion
        termino = input("Ingrese termino del glosario: ")
        definicion = input("Ingrese su definicion: ")
        #Agregamos elemento al diccionario
        res[termino] = definicion
    return res

#Muestra los valores del glosario
def mostrar_glosario(dic_glosario):
    lista_terminos = dic_glosario.keys()
    for termino in lista_terminos:
        print("*" * 30)        
        print("Termino:", termino)
        print("Definicion:", dic_glosario[termino])
        print("*" * 30)

if __name__ == "__main__":
    dic_glosario = leer_glosario()
    mostrar_glosario(dic_glosario)
