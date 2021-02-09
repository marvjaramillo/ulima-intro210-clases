import time
def es_primo3(n):
    cont = 3
    res = True
    if(n != 2 and (n == 1 or n % 2 == 0)):
        res = False
    else:
        while(cont * cont <= n and res == True):
                if(n % cont == 0):                                
                    res = False
                cont += 2
    return res

def evaluar(inicio, fin, incremento):
    for i in range(inicio, fin + 1, incremento):
        hora_inicio = time.time()
        es_primo3(i)
        hora_fin = time.time()
        duracion = hora_fin - hora_inicio
        print(i, duracion)

if __name__ == "__main__":
    evaluar(10 ** 8, 10 ** 9, 10000000)