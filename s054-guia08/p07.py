'''
Proponemos una estructura de diccionario. Clave -> dia de la semana.
Los valores seran listas. Las listas tendran varios cursos.
Cada curso tambien se representara con una lista.
En conclusion, trabajaremos con listas de listas

{
    "Lunes": [
                ["08:00", "01:00", "Base de Datos"], #primer curso
                ["10:00", "02:00", "Algoritmos"], #segundo curso
                ...
             ],
    "Martes": [],
    ....
}
'''
def registrar_horario():
    #La respuesta se almacenara en un diccionario
    horario = {}
    #El horario sera por dias de la semana
    #dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
    dias_semana = ["Lunes", "Martes"]
    for i in range(len(dias_semana)):
        dia = dias_semana[i]
        print("Ingrese horario para el dia", dia)
        cant_cursos = int(input("Ingrese cantidad de cursos para el " + dia +": "))
        lista_cursos = []
        for i in range(cant_cursos):
            hora_inicio = input("Ingrese hora inicio: ")
            duracion = input("Ingrese duracion: ")
            nombre = input("Ingrese nombre del curso: ")
            #La informacion del curso sera una lista
            informacion_curso = [hora_inicio, duracion, nombre]
            #Agregamos la informacion del curso a la lista de cursos
            lista_cursos.append(informacion_curso)
        #Agrego al diccionario la lista de cursos del dia de la semana correspondiente
        horario[dia] = lista_cursos
    return horario

if __name__ == "__main__":
    diccionario = registrar_horario()
    print(diccionario)