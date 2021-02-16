def evaluar(dic_paises):
    aciertos = 0
    #Por cada pais:    
    for pais in dic_paises.keys():
        #Imprimir la pregunta al estudiante y leer la respuesta
        respuesta = input("Ingrese la capital de " + pais + ": ")
        #Obtener la respuesta correcta (capital del pais)
        capital = dic_paises[pais]
        #Comparar lo ingresado con la respuesta
        #Si son iguales, se contabiliza el acierto
        if(respuesta == capital):
            aciertos = aciertos + 1
    print("Usted tuvo", aciertos, "aciertos")

if __name__ == "__main__":
    dic_paises = {"PERU": "LIMA", "ECUADOR": "QUITO", "COLOMBIA": "BOGOTA"}    
    evaluar(dic_paises)
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    