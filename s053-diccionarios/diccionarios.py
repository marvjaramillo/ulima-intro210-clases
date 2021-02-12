#Diccionario: alumnos y promedio ponderado
dic_alu = {"A01": 14.3, "A02": 15.1, "A03": 13.99}
print(dic_alu["A01"])

#Diccionario: alumnos y lista de notas
dic_alu2 = {"A01": [10, 12], "A02": [14, 15, 11], "A03": [18, 13]}

#Notas del alumno de codigo "A03"
print(dic_alu2["A03"])

#Segunda nota del alumno de codigo "A03"
print(dic_alu2["A03"][1])

#Promedio de notas del alumno "A02"
lista_notas = dic_alu2["A02"]
print(dic_alu2["A02"])
suma = 0
for i in range(len(lista_notas)):
    suma = suma + lista_notas[i]
print("El promedio es:", (suma / len(lista_notas)))

#Mostrar la lista de claves
for clave in dic_alu2.keys():
    print(clave)

#Mostras todas las listas de notas (valores)
for valor in dic_alu2.values():
    print(valor)