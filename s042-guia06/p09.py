def imprimir(n):						#   Mejor Caso          Peor Caso
    if(n >= 1 and n <= 20):             #       1                   1                           
        for i in range(n):              #       0                   n                            
            for j in range(2 * n):      #       0                  2n^2  
                print("*", end="")      #       0                  2n^2  
            print()                     #       0                   n
                                        #       -                   -
        for i in range(n):              #       0                   n
            for j in range(5 * n):      #       0                  5n^2
                print("*", end="")      #       0                  5n^2
            print()                     #       0                   n
                                        #   =========        ===============
#                           T(n) =              1             14n^2 + 4n + 1      


'''                 
Mejor Caso: Numero no esta en el intervalo [1, 20]
Peor Caso: Numero en el intervalo [1, 20]
Complejidad: O(n ^ 2)
'''
