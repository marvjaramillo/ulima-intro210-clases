'''
Solucion alternativa a la pregunta 1 (con funciones)
'''
def convertir(cod_moneda, monto):
    res = None
    if(cod_moneda == 1):
        res = 3.64 * monto
    elif(cod_moneda == 2):
        res = 4.42 * monto
    elif(cod_moneda == 3):
        res = 0.57 * monto
    return res

def main():
    codigo = int(input("Ingrese codigo de moneda: "))
    monto = int(input("Ingrese monto: "))

    cambio = convertir(codigo, monto)
    
    if(cambio != None):
        print("Monto equivalente en soles:", cambio)
    else:
        print("Codigo de moneda invalido")

if __name__ == "__main__":
    main()