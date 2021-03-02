import random
def generar_lista(cantidad, inicio, fin):
    lista = []
    for i in range(cantidad):
        valor = random.randint(inicio, fin)
        lista.append(valor)
    return lista