'''
Implemente una funcion que reciba un numero positivo N y retorne la suma de digitos
impares que tiene este numero
Ejm:
N = 789
Digitos impares: 7 y 9
Suma = 16

789 --> 9 ..... 789 % 10
78 --> 8
7 --> 7
0
'''
def suma_impares(N):
    suma = 0
    while(N > 0):
        #Obtengo el ultimo digito (derecha)
        ult_digito = N % 10
        #Verifico si es impar
        if(N % 2 != 0):
            #En caso afirmativo, lo agrego a la suma
            suma = suma + ult_digito
        #Le quito el ultimo digito a N
        N = N // 10
    return suma

def main():
    N = 678
    suma_dig = suma_impares(N)
    print("La suma de digitos impares es:", suma_dig)

if __name__ == "__main__":
    main()