#A)
def leer_datos():
    lista = []
    n = int(input("Ingrese el valor de 'n': "))
    for i  in range(n):
        valor = int(input("Ingrese valor:"))
        lista.append(valor)
    return lista

#B)
def generar_lista(lista):
    nueva_lista = []
    for i in range(len(lista)):
        if(lista[i] % 2 == 0 or lista[i] % 7 == 0):
            nueva_lista.append(lista[i])
    return nueva_lista

if __name__ == "__main__":
    lista = leer_datos()
    nueva = generar_lista(lista)
    print(lista)
    print(nueva)