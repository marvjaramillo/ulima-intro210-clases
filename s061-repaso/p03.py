'''
Los minutos de tardanza de un grupo de empleados se encuentran almacenados en un diccionario
que tiene como clave el codigo de empleado y como valor una lista con los minutos de 
tardanza por dia.
Implemente un programa que reciba este diccionario, un listado de codigos de empleado
y permita mostrar el empleado de la lista que tuvo la mayor cantidad de minutos acumulados
por tardanza.

Ejemplo:
dicc = {"E001": [5, 10, 3, 4], "E002": {}, "E003":[30, 10] }
lista = ["E001", "E003"]

E001 --> [5, 10, 3, 4] --> 22
E003 --> [30, 10] --> 40

Comparando los minutos de tardanza, el empleado con mayor cantidad de minutos de 
tardanza es "E003".
'''
def sumar_tardanzas(lista):
    suma = 0
    for i in range(len(lista)):
        suma = suma + lista[i]
    return suma

def mostrar_mayor_tardanza(dic_tardanzas, lista_empleados):
    cod_elegido = ""
    total_elegido = 0

    for i in range(len(lista_empleados)):
        cod_emp = lista_empleados[i]
        tardanzas_emp = dic_tardanzas[cod_emp]
        total_minutos = sumar_tardanzas(tardanzas_emp)
        if(total_minutos > total_elegido):
            total_elegido = total_minutos
            cod_elegido = cod_emp
    print("Empleado con mas minutos de tardanza:", cod_elegido)            
    print("Minutos de tardanza: ", total_elegido)

if __name__ == "__main__":
    dicc = {"E001": [50, 10, 3, 4], "E002": {}, "E003":[30, 10] }
    lista = ["E001", "E003"]
    mostrar_mayor_tardanza(dicc, lista)

