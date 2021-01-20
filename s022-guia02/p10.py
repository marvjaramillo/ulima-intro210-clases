tiempo_h = int(input("Ingrese cantidad de horas de estacionamiento: "))
tiempo_min = int(input("Ingrese cantidad de minutos de estacionamiento: "))

#Si se estaciono menos de una hora >> no se paga estacionamiento
if(tiempo_h == 0):
    print("No tiene que pagar estacionamiento")
else:
    #Si hay minutos (fraccion de hora) >> paga la hora completa
    if(tiempo_min > 0):
        tiempo_h = tiempo_h + 1
    #Pagar por las horas de estacionamiento
    monto = 2.5 * tiempo_h
    print("El monto por estacionamiento es:", monto)