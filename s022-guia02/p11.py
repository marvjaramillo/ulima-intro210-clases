# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 09:29:46 2020

@author: JC
"""
docenas = int(input("Ingrese cantidad a comprar (docenas): "))
precio = float(input("Ingrese precio por docena: "))

MIN_DOC_REGALO = 4

obsequios = 0
descuento = 0
monto = docenas * precio

#Descuento
if(docenas > 3):
    descuento = 0.15 * monto
else:
    descuento = 0.1 * monto

monto = monto - descuento
    
#Unidades
if(docenas >= MIN_DOC_REGALO):
    obsequios = docenas - MIN_DOC_REGALO + 1

print("Descuento: ", descuento)
print("Monto final: ", monto)
print("Obsequios: ", obsequios)

