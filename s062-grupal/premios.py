import random
MAXIMOS_INTENTOS = 5
def participar():
    numero = random.randint(1, 100)
    intentos = 0
    ganador = False
    print("<Para pruebas>: Numero generado:", numero)
    while(ganador == False and intentos < MAXIMOS_INTENTOS):
        apuesta = int(input("Adivine el valor entre 0 y 100: "))
        if(apuesta == numero):
            print("Ha adivinado el numero. Felicidades...")
            ganador = True
        else:
            print("Valor incorrecto")
            intentos = intentos + 1
    if(ganador == False):
        print("Ha utilizado todos los intentos disponibles...")