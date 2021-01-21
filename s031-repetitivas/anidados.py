'''
Implemente un programa que imprima en pantalla la siguiente matriz:
1 2 3
4 5 6
7 8 9
'''

def main():
    contador = 0
    for i in range(3):
        for j in range(3):
            contador = contador + 1
            print(contador, end = " ")
        print()
     
if __name__ == "__main__":
    main()