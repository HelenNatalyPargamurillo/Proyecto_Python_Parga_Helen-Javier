
import json

def informacion():
    while True:
        with open("inscripcion.json","r") as datos_cam:
            inscripcion=json.load(datos_cam)        #///carga archivo json en variable///
    
        ingreso={
            "N° de identificacion":int(input("numero de identificacion:")),
            "Nombres":(input("nombres:")),
            "Nombres":(input("nombres:")),
            "Apellido":(input("Apellido:")),
            "Acudiente":(input("Acudiente:")),
            "celular":int(input("celular:")),
            "estado":(input("estado actual del Camper:")),
        }
        inscripcion["campers"]["inscripcion"].append(ingreso)
        with open ("inscripcion.json","w") as datos:
            json.dump(inscripcion, datos, indent=4)

        print("su ingreso fue exitoso")

informacion()
