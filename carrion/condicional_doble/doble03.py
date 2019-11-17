import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
producto,costo,rebaja="",0.0,0.0

#INPUT
producto=os.sys.argv[1]
costo=float(os.sys.argv[2])
rebaja=float(os.sys.argv[3])

#PROCESSING
precio_total=round(costo-rebaja)

#VEREFICADOR
producto_calidad=(precio_total>=250)

#OUTPUT
print("###############################")
print("# BOLETA DE VENTA ")
print("###############################")
print("#")
print("#NOMBRE DEL PRODUCTO :",producto)
print("# PRECIO PRODUCTO    :",costo)
print("REBAJA               :",rebaja)
print("costo total s/.      :",precio_total)
print("###############################")
print("¿el producto es de alta calidad?:",producto_calidad)

#condicion doble
#si el producto es de calidad
if(precio_total==250):
    print("por realizar esta compra se 10 soles")
#fin_if

#agradecer al cliente
else:
    print("un gusto atenderle")
