from time import time
from p01 import es_primo1
from p02 import es_primo2

def evaluar(inicio, fin, incremento):
    for i in range(inicio, fin + 1, incremento):
        hora_inicio = time()
        es_primo1(i)
        hora_fin = time()
        duracion1 = hora_fin - hora_inicio

        hora_inicio = time()
        es_primo2(i)
        hora_fin = time()
        duracion2 = hora_fin - hora_inicio

        print(i, duracion1, duracion2)

if __name__ == "__main__":
    evaluar(10 ** 5, 10 ** 6, 50000)
