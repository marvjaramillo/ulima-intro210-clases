def fibonacci(n):
    #Casos base
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

def main():
    for i in range(31):
        print(fibonacci(i), end=" ")


main()