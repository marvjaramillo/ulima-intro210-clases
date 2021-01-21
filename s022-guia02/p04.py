# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 10:55:50 2020

@author: JC
"""

actual = int(input("Ingrese anio actual: "))
anio = int(input("Ingrese anio a analizar: "))

if(actual > anio):
    dif = actual - anio
    print("Han pasado", dif, "anios")
elif(actual < anio):
    dif = anio - actual
    print("Faltan", dif, "anios")
else:
    print("Anio ingresado coincide con el actual")