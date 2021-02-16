'''
a) Representacion para las cartas

- Tuplas: (valor, palo)

Valor: "A", "2", "3", ...., "J", "Q", "K"

Palos:
E: Espadas
T: Trebol
C: Corazones
D: Diamantes

b) Verificar si hay poker

Para resolver, crear un diccionario con la cantidad de apariciones de cada carta
Ejemplo:
{
    "A": 4,
    "8": 1
}
En el caso anterior, el As aparece 4 veces y el valor 8 aparece una sola vez.
'''
def obtener_apariciones(lista_cartas):
    #Diccionario de respuesta en blanco
    dic_apariciones = {}
    #Recorremos la lista de cartas
    for i in range(len(lista_cartas)):
        #Cada carta se representa como una tupla
        carta = lista_cartas[i]
        #El valor de la carta es el primer elemento de la tupla
        valor_carta = carta[0]
        #Si el valor de la carta ya ha aparecido
        if(valor_carta in dic_apariciones):
            #Incremento la cantidad de apariciones
            dic_apariciones[valor_carta] = dic_apariciones[valor_carta] + 1
        #En caso contrario
        else:
            #Registro el valor en el diccionario con conteo = 1
            dic_apariciones[valor_carta] = 1
    return dic_apariciones


#Precondicion: lista_cartas tiene 5 elementos
def hay_poker(lista_cartas):
    APARICIONES_POKER = 4
    res = False
    #Obtengo diccionario con la cantidad de apariciones
    dic_apariciones = obtener_apariciones(lista_cartas)
    #Obtenemos las cartas (valores) que han aparecido
    lista_cartas = list(dic_apariciones.keys())
    #Por cada carta que ha aparecido
    for i in range(len(lista_cartas)):
        #Obtenemos el valor de la carta
        valor_carta = lista_cartas[i]
        #Obtenemos la cantidad de apariciones
        cant_apariciones = dic_apariciones[valor_carta]
        #Si aparece 4 veces, podemos decir que hay poker
        if(cant_apariciones == APARICIONES_POKER):
            res = True
    return res

if __name__ == "__main__":
    cartas =    [
                    ("A", "T"), #As de Trebol
                    ("8", "E"), #8 de Espadas
                    ("A", "E"),
                    ("A", "C"),
                    ("J", "D"),
                ]
    print(hay_poker(cartas))



