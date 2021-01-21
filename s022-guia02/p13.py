# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 11:01:37 2020

@author: JC
"""
a = int(input("Ingrese numero: "))
b = int(input("Ingrese numero: "))
c = int(input("Ingrese numero: "))
d = int(input("Ingrese numero: "))
e = int(input("Ingrese numero: "))
f = int(input("Ingrese numero: "))

suma_pares = 0
suma_impares = 0

if(a % 2 == 0):
    print(a, "es par")
    suma_pares = suma_pares + a
else:
    print(a, "es impar")
    suma_impares = suma_impares + a
    
if(b % 2 == 0):
    print(b, "es par")
    suma_pares = suma_pares + b
else:
    print(b, "es impar")
    suma_impares = suma_impares + b

if(c % 2 == 0):
    print(c, "es par")
    suma_pares = suma_pares + c
else:
    print(c, "es impar")
    suma_impares = suma_impares + c
    
if(d % 2 == 0):
    print(d, "es par")
    suma_pares = suma_pares + d
else:
    print(d, "es impar")
    suma_impares = suma_impares + d
    
if(e % 2 == 0):
    print(e, "es par")
    suma_pares = suma_pares + e
else:
    print(e, "es impar")
    suma_impares = suma_impares + e

if(f % 2 == 0):
    print(f, "es par")
    suma_pares = suma_pares + f
else:
    print(f, "es impar")
    suma_impares = suma_impares + f
    
print("Suma de valores pares: ", suma_pares)
print("Suma de valores impares: ", suma_impares)
    
    
    
    
    
    
    