def main():
    A = int(input("Ingrese el valor de A: "))
    B = int(input("Ingrese el valor de B: "))
    C = int(input("Ingrese el valor de C: "))
    S = 0
    if(A / B > 30):
        S = (A / C) * B ** 3
    else:
        for i in range(2, 31, 2):
            S = S + i ** 2
    print("Valor de S:", S)

if __name__ == "__main__":
    main()