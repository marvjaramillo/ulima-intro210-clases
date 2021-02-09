def obtener_total(monto, pago_antes):	#   Mejor Caso          Peor Caso
    if(monto <= 5000):                  #       1                   1
        impuesto = 0.10                 #       1                   0                  
    elif(monto <= 10000):               #       0                   1                    
        impuesto = 0.08                 #       0                   0                           
    else:                               #       -                   -                    
        impuesto = 0.05                 #       0                   1   
    monto = monto * (1 + impuesto)      #       1                   1
    descuento = 0                       #       1                   1
    if(pago_antes == True):             #       1                   1
        descuento = monto * 0.15        #       0                   1       
    monto = monto - descuento           #       1                   1
    return monto                        #       1                   1
                                        #   =========           ==========
#                           T(n) =              7                   9                   
'''                 
Mejor Caso: monto <= 5000 y pago_antes == False
Peor Caso: monto > 10000 y pago_antes == True
Complejidad: O(1)
'''
