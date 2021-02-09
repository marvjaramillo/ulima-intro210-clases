#Precondicion: m > n
def mostrar_numeros(n, m):				#   Mejor Caso          Peor Caso
    for i in range(n, m + 1):           #    m - n + 1             m - n + 1     
        if(i % 2 == 0):                 #    m - n + 1             m - n + 1                           
            print(i, "es par")          #   (m-n+1) / 2           (m-n+1) / 2           
        else:                           #       -                   - 
            print(i, "es impar")        #   (m-n+1) / 2           (m-n+1) / 2                
                                        #  ================     ================
#                           T(n) =          3 * (m-n+1)           3 * (m-n+1)                
'''                 
Mejor Caso / Peor Caso: Es el mismo caso.
Siempre se evaluan todos los numeros en el intervalo
Complejidad: O(m - n)
'''
