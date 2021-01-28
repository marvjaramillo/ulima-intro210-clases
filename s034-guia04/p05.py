def promedio(a, b):
    return (a + b) / 2

def main():
    a = int(input("Ingrese a: "))
    b = int(input("Ingrese b: "))
    res = promedio(a, b)
    print("El promedio es:", res)

if __name__ == "__main__":
    main()