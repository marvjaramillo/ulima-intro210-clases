
def es_primo1(n):						#   Mejor Caso          Peor Caso
    cant = 0                            #       1                   1                           
    for i in range(1, n + 1):           #       n                   n                           
        if(n % i == 0):                 #       n                   n                                       
            cant = cant + 1             #       2                   ? (< n)                    
    if(cant == 2):                      #       1                   1                           
        return True                     #       1                   0
    else:                               #       -                   -
        return False                    #       0                   1
                                        #   =========           ==========
#                           T(n) =           2n + 5               3n + 3      
'''                 
Mejor Caso: Numero es primo (2 divisores)
Peor Caso: Numero en el intervalo con la mayor cantidad de divisores
Complejidad: O(n)
'''