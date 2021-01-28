def invertir(cadena):
    res = ""
    for letra in cadena:
        res = letra + res
    return res

def main():
    cadena = "abcd"
    invertida = invertir(cadena)
    print(invertida)

if __name__ == "__main__":
    main()