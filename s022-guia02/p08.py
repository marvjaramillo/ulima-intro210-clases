# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 09:12:06 2020

@author: JC
"""
anio = int(input("Ingrese valor de anio: "))
bisiesto = None

if(anio % 400 == 0):
    bisiesto = True    
elif(anio % 100 == 0):
    bisiesto = False
elif(anio % 4 == 0):
    bisiesto = True
else:
    bisiesto = False

if(bisiesto == True): #if(bisiesto)
    print("Anio es bisiesto")
else:
    print("Anio no es bisiesto")