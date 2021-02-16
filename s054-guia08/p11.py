def invertir(diccionario):
    #Crear un diccionario en blanco
    res = {}
    #Obtengo la lista del claves del diccionario
    lista_claves = list(diccionario.keys())

    #Por cada clave en el diccionario:
    for i in range(len(lista_claves)):
        #Obtengo el valor de la clave
        clave = lista_claves[i]
        #Obtengo el valor asociado a la clave
        valor = diccionario[clave]
        #Registro un nuevo valor en el diccionario de respuesta >> 
        # clave -> valor, valor -> clave
        res[valor] = clave
    return res

if __name__ == "__main__":
    dicc = {"F8J-232": "74847389", "BTN-445": "65434545", "ZBU-231": "44335231"}
    nuevo_dicc = invertir(dicc)
    print(nuevo_dicc)