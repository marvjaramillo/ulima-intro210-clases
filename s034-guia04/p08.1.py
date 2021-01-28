'''
Solucion alternativa del ejercicio 8. Usando solamente numeros
'''
def invertir(numero):
    res = 0
    while(numero > 0):
        digito = numero % 10
        res = res * 10 + digito
        numero = numero // 10
    return res

def es_palindromo(numero):
    palindromo = False
    numero_invertido = invertir(numero)
    if(numero == numero_invertido):
        palindromo = True
    return palindromo

def main():
    numero = int(input("Ingrese numero: "))
    res = es_palindromo(numero)
    if(res == True):
        print("Numero es palindromo")
    else:
        print("Numero no es palindromo")

if __name__ == "__main__":
    main()
