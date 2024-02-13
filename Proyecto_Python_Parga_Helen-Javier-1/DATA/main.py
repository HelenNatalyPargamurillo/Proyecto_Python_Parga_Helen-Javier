import json




print("-------------------")
print("----Bienvenido a Campusland----")
print("-------------------")
cond=True
while cond == True:
    print("-------------------")
    print("1. trainers")
    print("2. campers ")
    print("3. cordinador ")
    print("4. salir ")

    decision = int (input(""))
    if  decision ==1:
        print("-------------------")
        print("1. ver horario")
        print("2. ver sala")
        print("3. salir ")
        print("-------------------")
        quehago=int(input("ingresa"))
        print("")
        if (quehago== 2):
            print("si funciono")

    
    
    if  decision ==2:
        print("-------------------")
        print("1. salir")
        print("-------------------")
        
        quehago=int(input("ingresa"))
        print("")   
    
    if (decision== 1):
            break

    
    if  decision ==3:

        decision=int(input("""MENU PRINCIPAL:\n 1. Registrar Camper \n 2.Registra Prueba \n 3.Registra Entrenador 
                           \n 4. Registrar Camper en Area De Entrenamiento \n 5. Crear Ruta de Aprendizaje \n 6.Asignar Ruta De Aprendizaje 
                           \n 7. Camper En Riesgo \n 8. Matricular Camper \n 9. Reportes \n 10. Salida"""))
       
        quehago1=int(input("ingresa"))
        
        if (quehago1== 1):
           quehago1=int(input("indique su Opcion:\n 1. Nombre \n 2. Apellido \n 3. Direccion \n 4. Acudiente \n 5. Telefono \n 6. Estado"))
        
        


    datos = agregar_campers()

    with open("campers.json", "w+") as campers:
        json.dump(datos, campers, sort_keys=True, indent=4)