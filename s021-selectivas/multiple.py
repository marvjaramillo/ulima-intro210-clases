'''
Los resultados de el examen de Ingles en un Instituto manejan las siguientes descripciones
en funcion a las calificaciones obtenidas:

[0 - 30>: Nivel Basico
[30 - 60>: Nivel Intermedio
[60 - 100]: Nivel Avanzado

Implemente un programa que lea la calificacion y muestre la descripcion
'''

def main():
    calificacion = int(input("Ingrese calificacion: "))
    #Basico
    if(calificacion >= 0 and calificacion < 30):
        print("Nivel Basico")
    elif(calificacion >= 30 and calificacion < 60):
        print("Nivel Intermedio")
    elif(calificacion >= 60 and calificacion <= 100):
        print("Nivel Avanzado")
    else:
        print("La calificacion ingresada es incorrecta")
    print("Fin")
if __name__ == "__main__":
    main()
