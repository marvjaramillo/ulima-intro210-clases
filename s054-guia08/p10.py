'''
Ejemplo de datos de Entrada:

codigo  nombre  apellido  edad
200     Juan    Perez     20
201     Mariana Vargas    19

Podemos representarla como un diccionario
{
    200: ["Juan", "Perez", 20],
    201: ["Mariana", "Vargas", 19]
}

'''

def leer_datos(n):
    datos = {}
    for i in range(n):
        #Leemos datos del alumno
        print("Datos alumno ", i + 1, ":")
        codigo = int(input("Ingrese codigo de alumno: "))
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        edad = int(input("Ingrese edad: "))
        #Agregamos al diccionario utilizando el codigo como clave
        datos[codigo] = [nombre, apellido, edad]
    return datos

def mostrar_alumno(diccionario, codigo):
    #Verifico si el codigo ingresado esta en el diccionario
    if(codigo in diccionario):
        #Si se encuentra, obtengo la lista con los atributos del alumno
        lista_datos = diccionario[codigo]
        #Obtengo cada valor y lo muestro
        nombre = lista_datos[0]
        apellido = lista_datos[1]
        edad = lista_datos[2]
        print("Alumno encontrado:")
        print("Nombre:", nombre)
        print("Apellido:", apellido)
        print("Edad:", edad)
    else:
        print("No se encuentra el alumno")

if __name__ == "__main__":
    diccionario = leer_datos(3)
    print(diccionario)
    codigo_buscar = int(input("Ingrese codigo de alumno a buscar: "))
    mostrar_alumno(diccionario, codigo_buscar)
