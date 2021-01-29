def es_primo(digito):
    if(digito == 2 or digito == 3 or digito == 5 or digito == 7):
        return True
    else:
        return False

def suma_digitos_primos(n):
    suma = 0
    while(n > 0):
        digito = n % 10
        if(es_primo(digito)):
            suma = suma + digito
        n = n // 10
    return suma

def obtener_numero(n):
    res = 0
    while(n > 0):
        digito = n % 10
        if(es_primo(digito)):
            #Corremos el ultimo digito leido a la derecha (mult. * 10)
            #El digito leído debe ir a la derecha: lo sumamos
            res = res * 10 + digito
        n = n // 10
    return res

def main():
    N = 238749823499213165434
    suma = suma_digitos_primos(N)
    numero = obtener_numero(N)
    print("N =", N)
    print("Suma de digitos primos: ", suma)
    print("Numero obtenido con digitos primos:", numero)

if __name__ == "__main__":
    main()