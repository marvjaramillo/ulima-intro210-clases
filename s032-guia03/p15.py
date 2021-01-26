def main():
    A = int(input("Ingrese el valor de A: "))
    B = int(input("Ingrese el valor de B: "))
    S = 0
    if(A >= B):
        for i in range(10, 51, 2):
            S = S + i
    elif(A / B  <= 30):
        S = A ** 2 + B ** 2
    print("El valor de S es:", S)


if __name__ == "__main__":
    main()