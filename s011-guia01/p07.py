'''
Entrada: z
Salida: P(z)
P(x) = x ^ 4 + x ^ 3 + 2x ^ 2 - x
'''
z = float(input("Ingrese valor a evaluar:"))
resultado = z*z*z*z + z*z*z + 2*z*z - z
print("El resultado es:", resultado)