import os

#boleta de venta
#declaracion de variables
nombre,producto1,producto2="","",""
costo1,costo2=0.0,0.0
costo_total_productos=0.0

#input
nombre=os.sys.argv[1]
producto1=os.sys.argv[2]
costo1=float(os.sys.argv[3])
producto2=os.sys.argv[4]
costo2=float(os.sys.argv[5])

#procesing
costo_total_productos=round(costo1+costo2)

#verificador
costo_total_productos_pago=(costo_total_productos>20)

#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("# cliente         :",nombre)
print("# primer producto :",producto1,"  COSTO:",costo1)
print("# segundo producto:",producto2,"  COSTO:",costo2)
print("costo total s/.   :",costo_total_productos)
print("###############################")
print("los productos son de facil pago:",costo_total_productos_pago)

#condicional simple
#si el cliente gana si paga mayor que s/.50 un producto gratis
if(costo_total_productos_pago>50):
    print("utd ha ganado un producto gratis")
#fin_if
