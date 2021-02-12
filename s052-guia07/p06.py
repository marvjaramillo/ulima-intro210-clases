def obtener_lista(nombres, letra):
    #Lista de respuesta inicia en blanco
    respuesta = []
    #Recorrer la lista
    for i in range(len(nombres)):
        #Obtenemos el nombre
        nombre_persona = nombres[i]
        #Comparamos la primera letra del nombre con la letra dada como parametro
        if(nombre_persona[0] == letra):
            respuesta.append(nombre_persona)
    return respuesta

def main():
    nombres = ["Cesar", "Pedro", "Mariana", "Carlos", "Milagros"]
    lista = obtener_lista(nombres, "C")
    print(lista)

if __name__ == "__main__":
    main()