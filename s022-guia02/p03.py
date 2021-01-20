def main():
    a = int(input("Ingrese primer numero: "))
    b = int(input("Ingrese segundo numero: "))

    if(a > b):
        print("Primer numero es mayor")
    elif(b > a):
        print("Segundo numero es mayor")
    else:
        print("Numeros son iguales")
        
if __name__ == "__main__":
    main()