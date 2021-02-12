def obtener_maximo(lista):
    #Asumimos que el mayor valor es el primero
    mayor = lista[0]
    #Recorremos los siguientes elementos
    for i in range(1, len(lista)):
        #Si el elemento leido es el mayor, reemplazamos
        if(lista[i] > mayor):
            mayor = lista[i]
    return mayor

def obtener_calificaciones(lista):
    #Obtener mayor calificacion
    mayor = obtener_maximo(lista)
    #Definir una lista en blanco
    respuesta = []
    #Recorrer los elementos de la lista (cada nota)
    for i in range(len(lista)):
        #Almaceno la nota del alumno
        nota = lista[i]
        #Calcular la calificacion en letras    
        if(nota >= mayor - 2):
            calificacion = "A"
        elif(nota >= mayor - 4):
            calificacion = "B"
        elif(nota >= mayor - 6):
            calificacion = "C"
        elif(nota >= mayor - 8):
            calificacion = "D"
        else:
            calificacion = "E"
        respuesta.append(calificacion)
    return respuesta
        
def main():
    notas = [2, 10, 15, 13, 17, 16, 11, 11]
    lista_calificaciones = obtener_calificaciones(notas)
    print(notas)
    print(lista_calificaciones)

if __name__ == "__main__":
    main()