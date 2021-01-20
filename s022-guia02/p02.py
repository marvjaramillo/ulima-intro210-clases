dividendo = int(input("Ingrese dividendo: "))
divisor = int(input("Ingrese divisor: "))

if(divisor == 0):
    print("No es posible dividir entre cero")
else:
    if(dividendo % divisor == 0):
        print("Division es exacta")
    else:
        print("Division no es exacta")