'''
Los precios unitarios de un grupo de productos se encuentran almacenados en una lista L1
Las cantidades vendidas por cada uno se encuentran almacenadas en una lista L2, en el mismo
orden en que se encuentran en L1.
Se le solicita mostrar el producto que tuvo el menor volumen de ventas en dinero
y el monto total de dichas ventas

Ejemplo:
      P1   P2  P3
L1 = [10, 3.5, 5] #precios
L2 = [4, 2, 9] #cantidades

total = [40, 7, 45]
El menor volumen de ventas fue del producto 2
'''

def mostrar_menos_vendido(L1, L2):
    menor_volumen = L1[0] * L2[0]
    producto_seleccionado = 1
    for i in range(1, len(L1)):
        precio = L1[i]
        cantidad = L2[i]
        ventas = precio * cantidad
        if(ventas < menor_volumen):
            producto_seleccionado = i + 1
            menor_volumen = ventas
    print("Producto menos vendido: ", producto_seleccionado)
    print("Ventas: S/.", menor_volumen)


if __name__ == "__main__":
    L1 = [10, 3.5, 5] #precios
    L2 = [4, 2, 9] #cantidades    
    mostrar_menos_vendido(L1, L2)
