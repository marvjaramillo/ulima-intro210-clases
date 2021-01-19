'''
Entrada: peso_lb, estatura_pul
Salida: imc

Algoritmo:
**********
- Leer peso_lb, estatura_pul
- Convertir peso_lb a kg
- Convertir estatura_pul a m
- IMC = peso_kg / (estatura_m ^ 2)
1 libra equivale a 0.4536kilogramos y una pulgada equivale a 0.0254 metros
'''

peso_lb = float(input("Ingrese peso en libras: "))
estatura_pul = float(input("Ingrese estatura en pulgadas: "))

peso_kg = peso_lb * 0.4536
estatura_m = estatura_pul * 0.0254

imc = peso_kg / (estatura_m ** 2)
print("El IMC es:", imc)
