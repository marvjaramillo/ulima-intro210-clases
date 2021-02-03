def sumar_inversas(n):
    #Caso base: un solo numero
    if(n == 1):
        return 1
    else:
        #Recursion: el ultimo numero + suma de los anteriores
        return 1 / n + sumar_inversas(n - 1)

def main():
    res = sumar_inversas(12)
    print("Suma: ", res)

if __name__ == "__main__":
    main()