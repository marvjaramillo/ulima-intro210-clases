def factorial(n):
    print("Calculando factorial de: ", n)
    #Caso base
    if(n == 0):
        return 1
    else:
        #Recursion
        return n * factorial(n - 1)

def main():
    res = factorial(4)
    print(res)

main()