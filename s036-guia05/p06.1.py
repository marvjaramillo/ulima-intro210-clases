'''
Estrategia:
1) Leemos el valor como cadena (con el punto decimal)
2) LLamamos a una funcion para quitar el punto decimal
3) aplicamos la funcion que maneja enteros para hallar la suma de digitos
'''
import p06
def convertir(numero):
    res = ""
    #Convertimos a cadena para procesarlo
    numero = str(numero)
    for caracter in numero:
        if(caracter != "."):
            res = res + caracter
    #Convertimos la respuesta a entero
    return int(res)

def main():
    n = 49.89343
    print("Numero original:", n)
    n = convertir(n)
    print("Numero convertido:", n)
    suma_cifras = p06.suma_cifras(n)
    print("Suma de cifras:", suma_cifras)
        
if __name__ == "__main__":
    main()
