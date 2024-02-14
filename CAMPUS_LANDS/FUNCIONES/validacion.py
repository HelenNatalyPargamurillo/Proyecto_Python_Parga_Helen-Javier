
def eleccion():
    roles=True
    while roles :
        try:
            cordinacion = int (input("digite una opcion correcta: "))
            while not(1<=cordinacion <= 4):
                print ("por favor digite una opcion valida")    
                cordinacion = int (input("digite una opcion correcta: "))
        except ValueError:
            print("solo valores numericos")
        else :
            roles=False
    return cordinacion

def op_cord():
    roles=True
    while roles == True:
        try:
            cordinacion = int (input("digite una opcion correcta"))
            while not(1<=cordinacion <= 10):
                print ("por favor digite una opcion valida")    
                cordinacion = int (input("digite una opcion correcta"))
        except ValueError:
            print("solo valores numericos")
        else :
            roles=False
    return cordinacion

def nota():
    notas=True
    while  nota == True:
        try:
            cordinacion = int (input("digite una opcion correcta"))
            while not(1<=cordinacion <= 10):
                print ("por favor digite una opcion valida")    
                cordinacion = int (input("digite una opcion correcta"))
        except ValueError:
            print("solo valores numericos")
        else :
            roles=False
    return cordinacion

