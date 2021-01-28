def imprimir_matriz(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

def main():
    n = int(input("Ingrese orden de matriz: "))
    imprimir_matriz(n)

if __name__ == "__main__":
    main()