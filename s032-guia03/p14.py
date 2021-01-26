def main():
    n = int(input("Ingrese valor de n: "))    
    print("Los numeros que cumplen la condicion son:")
    suma = 0
    contador = 0
    producto = 1
    #Consiremos 2, 3, 4,  ..., n - 1
    for i in range(2, n):
        #Condicion: Multiplos de 2 y de 3
        #Alternativa: Multiplos de 6
        if(i % 2 == 0 and i % 3 == 0):
            #Imprimir el numero
            print(i)
            contador = contador + 1 #contador += 1
            suma = suma + i #suma += i
            producto = producto * i
    print("Cantidad de valores:", contador)
    print("Suma de valores:", suma)
    print("Producto de valores:", producto)    

if __name__ == "__main__":
    main()