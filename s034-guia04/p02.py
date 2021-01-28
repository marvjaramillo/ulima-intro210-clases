def es_vocal(caracter):
    res = False
    if(caracter == "a" or caracter == "A"):
        res = True
    elif(caracter == "e" or caracter == "E"):
        res = True
    elif(caracter == "i" or caracter == "I"):
        res = True
    elif(caracter == "o" or caracter == "O"):
        res = True
    elif(caracter == "u" or caracter == "U"):
        res = True
    return res

def main():
    chr = "a"
    res = es_vocal(chr)
    if(res == True):
        print("Es una vocal")
    else:
        print("No es una vocal")

if __name__ == "__main__":
    main()