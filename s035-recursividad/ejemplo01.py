'''
Se tiene una funcion G que recibe valores enteros mayores que cero
Se cumple la siguiente regla:
G(x) = 14 + 0.5 * G(x - 1), para x > 1
G(x) = 0, para x = 1
Implemente un programa recursivo que permita calcular el calbular el valor de G 
para un numero dado
'''

def G(x):
    #Caso base
    if(x == 1):
        return 0
    else:
        return 14 + 0.5 * G(x - 1)

def main():
    print(G(1))
    print(G(3))
    print(G(7))

main()