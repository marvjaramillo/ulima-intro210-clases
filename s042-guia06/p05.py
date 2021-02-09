def es_par(n):                          #   Mejor Caso          Peor Caso
    res = False                         #       1                   1
    if(n % 2 == 0):                     #       1                   1
        print("El numero es par")       #       0                   1
        res = True                      #       0                   1
    return res                          #       1                   1
                                        #   =========           ==========
#                           T(n) =              3                   5
'''                 
Mejor Caso: n impar
Peor Caso: n par
Complejidad: O()
'''