import time
def es_primo2(n):
    i = 3
    res = True
    while(i < n):
        if(n % i == 0):
            res = False
        i = i + 2
    if(n == 1):
        res = False
    elif(n != 2 and n % 2 == 0):
        res = False
    return res

def evaluar(inicio, fin, incremento):
    for i in range(inicio, fin + 1, incremento):
        hora_inicio = time.time()
        es_primo2(i)
        hora_fin = time.time()
        duracion = hora_fin - hora_inicio
        print(i, duracion)

if __name__ == "__main__":
    evaluar(10 ** 5, 10 ** 6, 10000)