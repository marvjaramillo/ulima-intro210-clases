'''
Un algoritmo para determinar si un numero es primo o no utiliza
la cantidad de divisores. Si el numero tiene 2 divisores, se dice
que dicho numero es primo.
Implemente un programa que reciba un entero N y que imprima en
pantalla los numeros primos en el intervalo [1, N]. Utilice el
algoritmo descrito para determinar si los numeros son primos
o no.
'''
'''
Permite determinar la cantidad de divisores de un numero N
Entrada: N, valor a evaluar
Salida: suma, cantidad de divisores del numero
'''

def cantidad_divisores(N):
    cantidad = 0
    for i in range(1, N + 1):
        if(N % i == 0):
            cantidad = cantidad + 1        
    return cantidad

'''
Permite determinar si un numero es primo o no
Entrada: N, valor a evaluar
Salida: res, Verdadero o Falso en funcion a lo evaluado
'''
def es_primo(N):
    cant_div = cantidad_divisores(N)
    if(cant_div == 2):
        res = True
    else:
        res = False
    return res

def main():
    N = 300
    for i in range(2, N + 1):
        if(es_primo(i) == True):
            print(i, end=" ")

if __name__ == "__main__":
    main()