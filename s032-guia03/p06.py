def main():
    inicio = 1
    fin = 52
    incremento = 3
    suma = 0
    for i in range(inicio, fin + 1, incremento):
        suma = suma + i
    print("La suma es:", suma)

if __name__ == "__main__":
    main()