import menu
import usuarios
import envios
import premios
def main():
    continuar = True
    while(continuar == True):
        menu.mostrar_menu()
        opcion = menu.obtener_opcion()
        if(opcion == menu.OPCION_COTIZAR):
            envios.cotizar()
        elif(opcion == menu.OPCION_PARTICIPAR):
            premios.participar()
        elif(opcion == menu.OPCION_DETENER):
            if(usuarios.validar_administrador() == True):
                continuar = False
            else:
                print("No puede detener la aplicacion...")
        elif(opcion == menu.OPCION_CREDITOS):
            mostrar_creditos()
        else:
            print("La opcion no es correcta")
    print("Gracias por utilizar la aplicacion")
    
def mostrar_creditos():
    print("Curso Introduccion a la Programacion")
    print("2021")

if __name__ == "__main__":
    main()