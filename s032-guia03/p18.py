def main():
    palabra = input("Ingrese palabra: ")
    n = int(input("Ingrese el valor de n: "))
    for i in range(n):
        for j in range(n):
            print(palabra, end="\t")
        print()

if __name__ == "__main__":
    main()