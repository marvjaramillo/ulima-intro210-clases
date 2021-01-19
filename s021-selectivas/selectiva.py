'''
Implemente un programa que lea la calificacion de un alumno y su cantidad de 
participaciones. Si la cantidad de participaciones es mayor que 10, entonces
recibe un punto de bonificacion. Su programa debe mostrar en pantalla la 
nota final
'''

def main():    
    nota = int(input("Ingrese nota: "))
    participaciones = int(input("Ingrese participaciones: "))
    #Si la cantidad de participaciones es mayor que 10
    if(participaciones > 10):
        #Incremento la nota en 1
        print("Felicidades, tiene un punto de bonificacion")        
        nota = nota + 1
    else:
        print("Lamentablemente no tiene bonificacion")
    print("Nota final:", nota)

if __name__ == "__main__":
    main()
