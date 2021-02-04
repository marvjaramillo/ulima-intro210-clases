import time
def calcular(n):
    res = 0
    for i in range(n):
        for j in range(n):
            res = res + 1
    return res

def main():
    for i in range(40, 3000, 100):
        #Almaceno la hora de inicio
        inicio = time.time()        
        #Programa que deseamos medir
        calcular(i)
        #Almaceno la hora de fin 
        fin = time.time()
        #Obtenemos el tiempo de duracion (* 1000: milisegundos)
        tiempo = (fin - inicio) * 1000
        print(i, tiempo)

if __name__ == "__main__":
    main()