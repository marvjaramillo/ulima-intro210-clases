'''
- Invertir numero
- Si el numero invertido es igual al numero original -> es palindromo. 
En caso contrario no lo es
'''
def invertir(cadena):
    res = ""
    for letra in cadena:
        res = letra + res
    return res

def es_palindromo(numero):
    palindromo = False
    numero_invertido = invertir(numero)
    if(numero == numero_invertido):
        palindromo = True
    return palindromo

def main():
    numero = input("Ingrese numero: ")
    res = es_palindromo(numero)
    if(res == True):
        print("Numero es palindromo")
    else:
        print("Numero no es palindromo")

if __name__ == "__main__":
    main()
