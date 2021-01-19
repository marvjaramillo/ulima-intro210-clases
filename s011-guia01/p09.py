'''
Entradas: N0, e (constante), t1, t2
Salidas: Nuevos infectados en el día 5 de abril.

Formula:
N(t) = N0 * e ^ (5t)

- 1 de abril: t = 0 (inicia la infeccion). Para el 5 de abril: t = 4
- "Nuevos infectados" reportados el 5 de abril: N(4) - N(3)
'''
N0 = 5
e = 2.72
#Casos del 5 de abril
t = 4
N4 = N0 * e ** (5 * t)

#Casos del 4 de abril
t = 3
N3 = N0 * e ** (5 * t)

#Nuevos infectados: N4 - N3
nuevos = N4 - N3
print("Casos nuevos reportados el 5 de abril: ", nuevos)