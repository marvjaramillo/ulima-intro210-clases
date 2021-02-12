def imprimir_instrucciones(productos):
    print("Ir a tienda")
    for i in range(len(productos)):
        print("Comprar", productos[i])
    n = len(productos)
    print("Pagar por los", n, "articulos")

def main():
    compras = ["papas", "leche", "huevos", "agua mineral"]
    imprimir_instrucciones(compras)

if __name__ == "__main__":
    main()