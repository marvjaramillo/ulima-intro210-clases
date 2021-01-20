def main():
    monto = float(input("Ingrese monto gastado: "))
    if(monto < 0):
        print("Valor del monto es incorrecto")
    elif(monto <= 100):
        print("Pago con dinero en efectivo")
    elif(monto < 300):
        print("Pago con tarjeta de debito")
    else:
        print("Pago con tarjeta de credito")

if __name__ == "__main__":
    main()