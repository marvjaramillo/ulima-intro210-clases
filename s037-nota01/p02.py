def main():
    N1 = int(input("Ingrese valor de N1: "))
    N2 = int(input("Ingrese valor de N2: "))
    cantidad = 0
    suma = 0
    for numero in range(N1, N2 + 1):
        seleccionado = False
        #Para saber si es primo, obtenemos la cantidad de divisores
        cant_div = 0
        for i in range(1, numero + 1):
            if(numero % i == 0):
                cant_div = cant_div + 1
        
        #Condicion: es primo
        if(cant_div == 2):
            seleccionado = True
        #Tiene 3 cifras
        elif(numero >= 100 and numero < 1000):
            seleccionado = True
        #Termina en 8
        elif(numero % 10 == 8):
            seleccionado = True
        
        if(seleccionado == True):
            print(numero, "cumple con las condiciones")
            cantidad = cantidad + 1
            suma = suma + numero
    print("Cantidad de numeros:", cantidad)
    print("Suma de numeros:", suma)

if __name__ == "__main__":
    main()