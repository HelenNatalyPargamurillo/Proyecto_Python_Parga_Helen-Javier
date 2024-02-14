import json

path = "CAMPUS_LANDS/Data/inscripcion.json"
path2="CAMPUS_LANDS/Data/notas.json"

with open("inscripcion.json" , "r") as archivo1:
    dato1=json.load(archivo1)

with open("ntas.json" , "r") as archivo2:
    dato1=json.load(archivo2)
   
