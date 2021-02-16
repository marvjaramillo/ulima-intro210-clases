def procesar_asistencia(emp):
    CODIGO_MAESTRO = 7777
    procesar = True

    while(procesar == True):
        codigo = int(input("Ingrese codigo: "))
        if(codigo != CODIGO_MAESTRO):
            #Se obtiene la lista con los datos del empleado
            datos_emp = emp[codigo]
            #Actualizamos la asistencia
            datos_emp[1] = True
            print("Asistencia registrada. Apellido: ", datos_emp[0])
        else:
            print("Codigo maestro ingresado ...")
            procesar = False

    print("Lista de empleados que no asistieron: ")
    asistencia = list(emp.values())

    for i in range(len(asistencia)):
        #Cada elemento sera una lista con el apellido del empleado y su asistencia
        asistencia_emp = asistencia[i]
        #El elemento 1 indica la asistencia del empleado
        if(asistencia_emp[1] == False):
            print(asistencia_emp[0])

if __name__ == "__main__":
    emp = {500: ["Perez", False], 600: ["Alvarez", False], 700: ["Gonzales", False]}
    procesar_asistencia(emp)


