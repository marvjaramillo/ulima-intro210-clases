def main():
    n = int(input("Ingrese valor de 'n': "))
    for i in range(1, n + 1):
        if(i % 2 != 0):
            print(i)

if __name__ == "__main__":
    main()