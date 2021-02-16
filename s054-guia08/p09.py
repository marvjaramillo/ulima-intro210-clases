def mostrar_colores(dic_colores):
    continuar = True
    while(continuar == True):
        codigo = int(input("Ingrese codigo de color: "))
        if(codigo != 0):
            color = dic_colores[codigo]
            print("El color seleccionado es:", color)
        else:
            continuar = False

if __name__ == "__main__":
    dic_colores = {1: "azul", 2: "verde", 3: "rojo", 4: "amarillo", 5: "naranja"}
    mostrar_colores(dic_colores)
