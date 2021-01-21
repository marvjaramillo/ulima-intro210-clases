a = int(input("Ingrese valor de a: "))
b = int(input("Ingrese valor de b: "))

if(b > a):
    print(b, "no puede ser divisor de", a)
else:
    if(a % b == 0):
        print(b, "es divisor de", a )
    else:
        print(b, "no es divisor de", a )