import time

def es_primo1(n):
    cant = 0
    for i in range(1, n + 1):
        if(n % i == 0):
            cant = cant + 1
    if(cant == 2):
        return True
    else:
        return False
    
def evaluar(inicio, fin, incremento):
    for i in range(inicio, fin + 1, incremento):
        hora_inicio = time.time()
        es_primo1(i)
        hora_fin = time.time()
        duracion = hora_fin - hora_inicio
        print(i, duracion)

if __name__ == "__main__":
    evaluar(10 ** 4, 10 ** 5, 500)