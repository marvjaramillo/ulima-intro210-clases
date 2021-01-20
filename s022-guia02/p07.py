def main():
    deposito = float(input("Ingrese monto de deposito: "))
    if(deposito <= 1000):
        #Se paga el 4% como interes        
        interes = 0.04 * deposito
    elif(deposito <= 5000):
        #Se paga el 5% de interes
        interes = 0.05 * deposito
    else:
        interes = 0.08 * deposito        
    print("El monto del interes es", interes)

if __name__ == "__main__":
    main()