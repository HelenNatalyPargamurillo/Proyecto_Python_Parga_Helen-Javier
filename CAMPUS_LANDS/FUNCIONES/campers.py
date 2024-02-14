
import json

path = "CAMPUS_LANDS/Data/inscripcion.json"



def validacion_id():
    val_num=True
    while val_num==True:
        try:
            id=int(input("numero de identificacion:"))
            while not(id>=1):
                print ("por favor digite una opcion valida")    
                id = int (input("digite una opcion correcta: "))
        except ValueError:
            print("solo valores numericos")
        else:
            val_num=False
    return id
        

def cel():
    val_num=True
    while val_num==True:
            try:
               cel=int(input("ingrese nota:"))
               while not(cel>=1):
                print ("por favor digite una opcion valida")    
                cel = int (input("digite una opcion correcta: "))
            except ValueError:
                print("solo valores numericos")
            else:
                val_num=False
def informacion():
    while True:
        #Cargar Datos
        inscripccion = {}
        with open(path ,"r") as archivo:
            inscripccion.update(json.load(archivo))        #///carga archivo json en variable///
        
            
        # val_num=True
            
        # while val_num==True:
        #     try:
        #        cel=int(input("numero de identificacion:"))
        #        while not(cel>=1):
        #         print ("por favor digite una opcion valida")    
        #         cel = int (input("digite una opcion correcta: "))
        #     except ValueError:
        #         print("solo valores numericos")
        #     else:
        #         val_num=False

        # val_num=True
    
        # while val_num==True:
        #     try:
        #        nt=int(input("numero de identificacion:"))
        #        while not(nt>=1):
        #         print ("por favor digite una opcion valida")    
        #         nt = int (input("digite una opcion correcta: "))
        #     except ValueError:
        #         print("solo valores numericos")
        #     else:
        #         val_num=False


            
            
        #Manejo de Datos
        ingreso={
            "N de identificacion":validacion_id(),
            "Nombres":(input("nombres:")),
            "Apellido":(input("Apellido:")),
            "Acudiente":(input("Acudiente:")),
            "celular":cel(),
            "estado":"inscrito",
            "nota":""
        }

        inscripccion["campers"].update({ingreso["N de identificacion"]: ingreso})

        #Guardar Datos
        with open (path, "w") as archivo:
            json.dump(inscripccion, archivo, indent=4)

        print("su ingreso fue exitoso")

        break

def notas():
        edit = open("CAMPUS_LANDS/Data/inscripcion.json")
        Dat = json.load(edit)
        camp = Dat["campers"]
        ID_camper = int(input("Ingrese el número de identificación del camper :"))
        for camp in camp:
            if camp["N de identificacion"] == ID_camper:

                teo = float(input("Ingrese promedio de notas de la teorica: "))
                pra = float(input("Ingrese promedio de notas de la practica: "))
                pro = float(input("Ingrese promedio da la procedimental: "))
                final = (teo *  0.3) + (pra *  0.6) + (pro *  0.1)
                if final >=  60:
                    camp['Estado'] = "Aprobado"
                    camp["nota"] = ("",final) 
                    print("¡Este camper ha aprobado el filtro mensual con una nota final de", final)
                
                else:
                    camp['Estado'] = "Reprobado"
                    camp["nota"] = "la nota es",final
                    print("El camper no ha aprobado, Su nota final es", final)
            else:
                print("Camper no encontrado.")
                break
