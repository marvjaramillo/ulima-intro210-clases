def factorial(n):
    if(n == 0):
        return 1
    else:
        return n * factorial(n - 1)

def main():
    n = int(input("Ingrese valor: "))
    res = factorial(n)
    print("Factorial: ", res)

if __name__ == "__main__":
    main()
    