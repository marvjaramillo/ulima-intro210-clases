'''
Implemente un programa que lea 6 valores enteros de teclado y calcula la suma de ellos
'''
def main():
    suma = 0
    n = int(input("Ingrese cantidad de valores a leer: "))
    for i in range(n):
        valor = int(input("Ingrese valor: "))
        suma = suma + valor
    print("La suma es: ", suma)

if __name__ == "__main__":
    main()