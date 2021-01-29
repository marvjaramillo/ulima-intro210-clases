'''
Solucion alternativa al ejercicio 2 (funciones)
'''

def es_primo(n):
    cant_div = 0
    for i in range(1, n + 1):
        if(n % i == 0):
            cant_div = cant_div + 1
    if(cant_div == 2):
        return True
    else:
        return False

def termina_8(n):
    if(n % 10 == 8):
        return True
    else:
        return False

def tiene_3_cifras(n):
    if(n >= 100 and n < 100):
        return True
    else:
        return False

def main():
    N1 = int(input("Ingrese valor de N1: "))
    N2 = int(input("Ingrese valor de N2: "))
    cantidad = 0
    suma = 0
    for numero in range(N1, N2 + 1):
        if(es_primo(numero) or tiene_3_cifras(numero) or termina_8(numero)):
            print(numero, "cumple con las condiciones")
            cantidad = cantidad + 1
            suma = suma + numero
    
    print("Cantidad de numeros:", cantidad)
    print("Suma de numeros:", suma)

if __name__ == "__main__":
    main()