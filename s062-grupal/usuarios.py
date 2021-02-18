USUARIOS_ADMINISTRADORES = ["jperez", "acordova"]
PASSWORDS_ADMINISTRADORES = ["password", "123456"] 

def validar_administrador():
    res = False
    usuario = input("Ingrese nombre de usuario administrador: ")
    password = input("Ingrese password de usuario administrador: ")    
    for i in range(len(USUARIOS_ADMINISTRADORES)):
        if(usuario == USUARIOS_ADMINISTRADORES[i]):
            if(password == PASSWORDS_ADMINISTRADORES[i]):
                res = True
    return res