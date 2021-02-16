'''
Registraremos la asistencia en un diccionario con este formato
clave: dia de la semana
valor: tupla con horas y minutos de la asistencia del empleado
{
    "Lunes": (10, 20),
    "Martes: (8, 35),
    "Miercoles: (11, 50), ....
}

'''
def registrar_asistencia():
    #Lista con dias de la semana
    dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
    #Diccionario de respuesta en blanco
    asistencia = {}
    #Por cada dia de la semana
    for i in range(len(dias_semana)):
        dia = dias_semana[i]
        print("Asistencia", dia)
        #Registramos hora y minutos de llegada
        hora = int(input("Digite hora de ingreso (h): "))
        minutos = int(input("Digite los minutos correspondientes: "))
        #Agregar un elemento al diccionario de asistencia
        asistencia[dia] = (hora, minutos)
    return asistencia

def calcular_tardanza(asistencia):
    HORA_INGRESO = 8
    minutos_tardanza = 0    
    #Por cada dia de la semana
    for dia_semana in asistencia.keys():
        #hora_entrada es una tupla con hora y minutos
        hora_entrada = asistencia[dia_semana]
        #Obtenemos cada valor
        hora = hora_entrada[0]
        minutos = hora_entrada[1]
        #Si la hora de entrada debe ser mayor o igual que el horario de ingreso
        if(hora >= HORA_INGRESO):
            #Contabilizar la tardanza: horas_tardanza * 60 + minutos
            minutos_tardanza += ((hora - HORA_INGRESO) * 60 + minutos)
    return minutos_tardanza

if __name__ == "__main__":
    asistencia = registrar_asistencia()
    print(asistencia)
    tardanza = calcular_tardanza(asistencia)
    print("Minutos de tardanza: ", tardanza)
