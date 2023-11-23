#DeclaracionDeVariables
Iva=0
PreO=0
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