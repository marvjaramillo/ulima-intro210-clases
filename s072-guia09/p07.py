def leer_datos(valor_escape):
    lista = []
    continuar = True
    while(continuar):
        valor = input("Ingrese palabra o 'NO' para terminar: ")
        if(valor != valor_escape):
            lista.append(valor)
        else:
            continuar = False

    return lista

def contar_palindromos(lista):
    contador = 0
    for i in range(len(lista)):
        palabra = lista[i]
        if(palabra == palabra[::-1]):
            contador = contador + 1
    return contador

if __name__ == "__main__":
    lista = leer_datos("NO")
    cantidad = contar_palindromos(lista)
    print("Cantidad de palindromos:", cantidad)