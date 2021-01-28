'''
Solucion alternativa del ejercicio 8. Importando la funcion de la pregunta 4
'''
import p04

def es_palindromo(numero):
    palindromo = False
    numero_invertido = p04.invertir(numero)
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
