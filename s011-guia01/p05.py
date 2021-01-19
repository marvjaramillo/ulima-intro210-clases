'''
Entrada: vf, vi, t
Salida: a (aceleracion)
'''
vi = float(input("Ingrese la velocidad inicial: "))
vf = float(input("Ingrese la velocidad final: "))
t = float(input("Ingrese el tiempo: "))

a = (vf-vi) / t
print("La aceleracion es:", a, "m/s^2")
