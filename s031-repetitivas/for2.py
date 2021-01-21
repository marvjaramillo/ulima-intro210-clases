n = 5
#range recibe un parametro
for i in range(n): #[0, n>
    print(i, end=" ")

print()

#range recibe dos parametros
for i in range(1, n + 1): #[1, n + 1>
    print(i, end=" ")

print()
n = 18
#range recibe tres parametros
for i in range(2, n + 1, 2): #[2, 19>, avanza de 2 en 2
    print(i, end=" ")

print()
for i in range(40, 0, -2): #40 hasta 1 (no incluye 0), disminuye de 2 en 2
    print(i, end=" ")