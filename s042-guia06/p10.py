def imprimir_matriz(n, m):					#   Mejor Caso          Peor Caso
    if(n < 100):                            #      1                    1
        for i in range(n):                  #      0                    n 
            for j in range(m):              #      0                  m * n  
                valor = (i * m) + (j + 1)   #      0                  m * n  
                print(valor, end="\t")      #      0                  m * n  
            print()                         #      0                    n
                                            #   =========          =============
#                           T(n) =                 1                3mn + 2n + 1  
'''                 
Mejor Caso: n >= 100
Peor Caso: n < 100
Complejidad: O(m * n)
'''
