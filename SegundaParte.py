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

#DesarrolladoPorAngel