def main():
    n = int(input("Ingrese el valor de n: "))
    cantidad = 4
    for i in range(n):
        for j in range(cantidad):
            print("*", end="")
        cantidad = cantidad + 4
        print()

if __name__ == "__main__":
    main()