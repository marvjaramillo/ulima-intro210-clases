'''
Objetivo: Imprimir en pantalla los "n" primeros numeros naturales >> [1, n]
'''
def imprimir_numeros(n):
    for i in range(1, n + 1):
        print(i, end=" ")
    print()

def main():
    for i in range(1, 26):
        print(i)

if __name__ == "__main__":
    imprimir_numeros(10)
    imprimir_numeros(18)
    imprimir_numeros(25)