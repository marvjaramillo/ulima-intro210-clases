'''
Implemente un programa que reciba un numero "n" y calcule la cantidad de sus divisores.
Ejemplo:
4 --> 1, 2, 4
Podemos decir que 4 tiene 3 divisores
'''
def main():
    n = int(input("Ingrese numero: "))
    cantidad = 0
    for i in range(1, n + 1): #[1, n + 1>: 1, 2, 3, 4, ...., n
        #Buscamos divisores: "i" es divisor de "n" si el residuo de la division es cero
        if(n % i == 0):
            cantidad = cantidad + 1
    print("Cantidad de divisores:", cantidad)
if __name__ == "__main__":
    main()