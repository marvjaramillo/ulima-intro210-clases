# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 09:44:03 2020

@author: JC
"""
'''' 
op2: Valor entero positivo
'''

op1 = int(input("Ingrese operando 1: "))
operacion = input("Ingrese operacion: ")
op2 = int(input("Ingrese operando 2: "))

resultado = 0
if(operacion == "+"):
    resultado = op1 + op2
elif(operacion == "-"):
    resultado = op1 - op2
elif(operacion == "*"):
    resultado = op1 * op2
elif(operacion == "/"):
    resultado = op1 / op2
else:
    resultado = None

if(resultado != None):
    print("Resultado: ", resultado)
else:
    print("Operador incorrecto")

