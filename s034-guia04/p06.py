'''
Funcion que calcula el factorial de un enter n.
Precondicion: n >= 0
'''
def factorial(n):
    res = 1
    if(n > 0):
        for i in range(2, n + 1):
            res = res * i
    return res

def main():
    res = factorial(6)
    print(res)

if __name__ == "__main__":
    main()
    