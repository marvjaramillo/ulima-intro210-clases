def convertir_digito(n):
    if(n < 10):
        return str(n)
    elif(n == 10):
        return "A"
    elif(n == 11):
        return "B"
    elif(n == 12):
        return "C"
    elif(n == 13):
        return "D"
    elif(n == 14):
        return "E"
    elif(n == 15):
        return "F"

def convertir(n, base):
    #Caso base: numero es cero (base fue mayor en la ejecucion previa)
    if(n == 0):
        res = ""
    else:
        cociente = n // base
        residuo = n % base
        res = convertir(cociente, base) + convertir_digito(residuo)
    return res

def main():
    res = convertir(2346374, 16)
    print(res)

if __name__ == "__main__":
    main()
