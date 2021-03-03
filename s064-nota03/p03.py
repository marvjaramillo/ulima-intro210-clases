def mostrar_recomendacion(personajes, jugador1, jugador2):
    poderes1 = personajes[jugador1]
    poderes2 = personajes[jugador2]

    poder_ataque1 = poderes1[0]
    poder_defensa1 = poderes1[1]

    poder_ataque2 = poderes2[0]
    poder_defensa2 = poderes2[1]

    ganador = None

    if(poder_ataque1 > poder_ataque2):
        ganador = jugador1
    elif(poder_ataque2 > poder_ataque1):
        ganador = jugador2
    else:
        if(poder_defensa1 > poder_defensa2):
            ganador = jugador1
        elif(poder_defensa2 > poder_defensa1):
            ganador = jugador2

    if(ganador != None):
        print("Se recomienda elegir a:", ganador)
    else:
        print("Ambos luchadores tienen las mismas habilidades")

if __name__ == "__main__":
    dicc = {"George G": [250, 80], "Ken T": [250, 175], "M Byrne": [60, 60]}
    jugador1 = "George G"
    jugador2 = "Ken T"
    mostrar_recomendacion(dicc, jugador1, jugador2)