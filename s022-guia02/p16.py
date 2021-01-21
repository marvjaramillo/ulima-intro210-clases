# -*- coding: utf-8 -*-
a = int(input("Ingrese lado mayor: "))
b = int(input("Ingrese lado 2: "))
c = int(input("Ingrese lado 3: "))

res = b ** 2 + c ** 2
if(a ** 2 == res):
    print("Es una terna pitagorica")
else:
    print("No es una terna pitagorica")