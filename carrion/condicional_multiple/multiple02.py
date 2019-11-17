import os

#boleta de venta
#declaracion de variabes
nombre,cant_producto="",0.0
precio=0.0
#input
nombre=os.sys.argv[1]
cant_producto=int(os.sys.argv[2])
precio=float(os.sys.argv[3])

#procesing
precio_total=round(cant_producto*precio)

#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("# cliente           :",nombre)
print("#NOMBRE DEL PRODUCTO:",cant_producto)
print("# PRECIO PRODUCTO   :",precio)
print("costo total s/.     :",precio_total)
print("###############################")

#condicional simple
#el cliente se gana un paneton si supera el precio total
#inicio_if
if(precio_total>50):
    print("felicidades,ha ganado un paneton")
#fin_if

#si el precio total esmenor que s/.50 se imprime:"si se lleva mas productos le regalamos un paneton"
#inicio_if
if(precio_total<50):
    print("si se lleva mas productos le regalamos un paneton")
#fin_if


#inicio_if
if(precio_total==50):
    print("casi logra llevarse un paneton")
#fin_if
