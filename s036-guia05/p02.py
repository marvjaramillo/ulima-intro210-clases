def potencia(base, exponente):
    #Caso base: exponente es cero - resultado es 1
    if(exponente == 0):
        return 1
    else:
        return base * potencia(base, exponente - 1)

def main():
    res = potencia(2, 6)
    print("Potencia: ", res)

if __name__ == "__main__":
    main()
    