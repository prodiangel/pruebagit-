#DeclaracionDeVariables
Iva=0
PreO=0
VlrBase=0
VlrIva=0
Operacion=""

#EntradaDeDatos
Operacion=str(input("¿Que Deseas Hacer,Calcular El Precio Con Iva o Sin Iva?"))

#DecicionDeVariable
if (Operacion == "Con Iva") or (Operacion == "con iva"):
    #EntradaDeDatos
    Iva=float(input("De cuanto Es la Tarifa Del Iva (Sin %)"))
    PreO=float(input("Inserta  El Precio Del Producto"))

    #Proceso
    Iva=(Iva/100)
    Iva=(PreO*Iva)
    PreO=(PreO+Iva)

    #Salida
    print("El Valor Del Iva Fue De ",Iva)
    print("El Precio Con El Iva Agregado Es De ",PreO)
else:
    if (Operacion==" Sin Iva") or (Operacion=="sin iva"):
        #DeclaracionDeVariables
        VlrBase=0
        VlrIva=0
        Iva=0

        #EntradaDeDatos
        VlrIva=float(input("Cuanto Cuesta El Producto"))
        Iva=float(input("Escribe La Tarifa Del Iva (Sin % ))"))

        #Proceso
        Iva=(Iva/100)
        VlrBase=(VlrIva)/(1+Iva)

        #Salida
        print("El Precio Original Es De ", VlrBase)
        print ("El Iva Fue De ",Iva)
    else:
        print("Te Equivocaste y Escribiste ",Operacion)
#DesarrolladoPorAngel
print("hola mundo")