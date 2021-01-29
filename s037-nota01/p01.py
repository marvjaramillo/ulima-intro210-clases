def main():
    codigo = int(input("Ingrese codigo de moneda: "))
    monto = int(input("Ingrese monto: "))
    res = None
    if(codigo == 1):
        res = 3.64 * monto
    elif(codigo == 2):
        res = 4.42 * monto
    elif(codigo == 3):
        res = 0.57 * monto
    
    if(res != None):
        print("Monto equivalente en soles:", res)
    else:
        print("Codigo de moneda invalido")

if __name__ == "__main__":
    main()