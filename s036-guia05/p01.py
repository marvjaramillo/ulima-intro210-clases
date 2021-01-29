def sumar_numeros(n):
    if(n == 1):
        return 1
    else:
        return n + sumar_numeros(n - 1)

def main():
    res = sumar_numeros(12)
    print("Suma: ", res)

if __name__ == "__main__":
    main()