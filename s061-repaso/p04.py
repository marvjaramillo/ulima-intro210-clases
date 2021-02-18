'''
Los datos de los empleados de una empresa se encuentran almacenados en un diccionario 
cuya clave es el codigo de empleado y cuyo valor es una lista formada por los siguientes
datos: [apellido, salario, edad]
Implemente un programa que reciba el diccionario mencionado y muestre en pantalla el
apellido del empleado de mayor salario
'''

def mostrar_mayor_salario(empleados):
    mayor = 0
    apellido_mayor = ""
    for codigo in empleados.keys():
        datos_emp = empleados[codigo]
        apellido = datos_emp[0]
        salario = datos_emp[1]
        if(salario > mayor):
            mayor = salario
            apellido_mayor = apellido

    print("El empleado", apellido_mayor, "es el de mayor salario")
    print("Salario:", mayor)

if __name__ == "__main__":
    dicc = {"E001": ["Perez", 3000, 12], "E002": ["Alvarez", 5000, 18]}
    mostrar_mayor_salario(dicc)
