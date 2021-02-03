def suma_cifras(n):
    #Caso base: el numero es cero
    if(n == 0):
        return 0
    else:
        #Recursion: ult_digito + numero luego de quitar el ult. digito
        ult_digito = n % 10
        nuevo_n = n // 10
        return ult_digito + suma_cifras(nuevo_n)

def main():
    n = 34874
    res = suma_cifras(n)
    print("Suma cifras:", res)

if __name__ == "__main__":
    main()