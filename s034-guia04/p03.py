def mult():
    n = 1
    mult = 1
    while(n != 0):        
        mult = mult * n
        n = int(input("Ingrese valor: "))
    return mult

def suma():
    n = -1
    suma = 0
    while(n != 0):
        n = int(input("Ingrese valor: "))
        suma = suma + n
    return suma

def main():
    res = suma()
    print("La suma de valores es:", res)

    res = mult()
    print("El producto de valores es:", res)

if __name__ == "__main__":
    main()