import FUNCIONES.validacion as valida
import FUNCIONES.titulos_op as titulo
import FUNCIONES.campers as informaciones

import os

programa={
    "campers":{}
}

campers={
    "nombre":"",
    "apellido":"",
    "direccion":"",
    "acudiente":"",
    "telefono":"",
    "estado":""

}

def inicio():
    titulo.rol()
    op_rol=valida.eleccion()
    os.system("clear")
    if op_rol== 1 :
        titulo.men_c()
        op_cord=valida.op_cord()
        
        if op_cord == 1:

            informaciones.informacion()  
        

        elif op_cord == 2:
            
            informaciones.notas()
            inicio()

        
        elif op_cord == 3:
            pass

    
        elif op_cord == 4:
            pass
        
        elif op_cord == 5:
            pass


        elif op_cord == 6:
            pass
        
        elif op_cord == 7:
            pass

    
        elif op_cord == 8:
            pass
        
        elif op_cord == 9:
            pass

        else :
            inicio()

if __name__ =="__main__":
    inicio()

