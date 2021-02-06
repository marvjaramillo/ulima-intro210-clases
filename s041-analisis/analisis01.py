def programa(n):                    #Mejor Caso     Peor caso  
    res = 0                         #   1               1
    if(n % 2 == 0):                 #   1               1
        for i in range(n):          #   0               n
            res = res + 1           #   0               n
    else:
        res = 26                    #   1               0
    return res                      #   1               1
                                    #________      ___________
                                    #   4             2n + 3
'''
Encontramos que, para el peor caso:
T(n) = 2n + 3
Utilizando notacion Big-O tendríamos que se trata de O(n)
'''