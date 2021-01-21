# -*- coding: utf-8 -*-
'''
Objetivo:
    Determinar si un numero es divisor de otro
Entradas:
    a, b - valores enteros
Salida:
    mensaje - indicando si b es divisor de a
'''
a = int(input("Ingrese valor de a: "))
b = int(input("Ingrese valor de b: "))

if(b > a):
    print(b, "no puede ser divisor de", a)
else:
    if(a % b == 0):
        print(b, "es divisor de", a )
    else:
        print(b, "no es divisor de", a )