archivo = open("data/docentes.csv")
for linea in archivo:
    datos_docente = linea.split(",")
    codigo = int(datos_docente[0])
    nombre = datos_docente[1]
    edad = int(datos_docente[2])
    print("Codigo:", codigo)
    print("Nombre:", nombre)
    print("Edad:", edad)
    print()