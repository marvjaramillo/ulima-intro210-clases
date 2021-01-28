def mostrar_conversiones(segundos):
    dias = segundos // 86400
    segundos = segundos % 86400
    horas = segundos // 3600
    segundos = segundos % 3600
    minutos = segundos // 60
    segundos = segundos % 60
    print("El equivalente es:")
    print(dias, "dia(s)")
    print(horas, "hora(s)")
    print(minutos, "minuto(s)")
    print(segundos, "segundo(s)")

def main():
    mostrar_conversiones(125637)

if __name__ == "__main__":
    main()