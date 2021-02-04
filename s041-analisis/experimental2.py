import time
def calcular(n):
    res = 0
    for i in range(n):
        for j in range(n):
            res = res + 1
    return res

def calcular2(n):
    res = 0
    for i in range(n):
        res = res + n
    return res

def main():
    for i in range(2000, 6000, 200):
        inicio = time.time()        
        calcular2(i)
        fin = time.time()
        tiempo1 = (fin - inicio) * 1000

        inicio = time.time()
        calcular(i)        
        fin = time.time()
        tiempo2 = (fin - inicio) * 1000        
        print(i, tiempo1, tiempo2)

if __name__ == "__main__":
    main()