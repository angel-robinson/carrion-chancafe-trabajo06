import os
#boleta
#declaracion de variables
nombre,mesas,precio_mesa="",0,0.0
pago_total=0.0
#input
nombre=os.sys.argv[1]
mesas=int(os.sys.argv[2])
precio_mesa=float(os.sys.argv[3])
#procesing
pago_total=round(precio_mesa*mesas)
#vereficador
cantidad=(pago_total>100)
#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("# el cliente es            :",nombre)
print("# numero total de lapiceros:",mesas)
print("# precio de cada lapicero  :",precio_mesa)
print("# pago total               :",pago_total)
print("###############################")
print("¿pago es mayor que 100 ?:",cantidad)
#si el cliente se lleva pasa de los s/.300, se lleba una silla gratis
#inicio_if
if(pago_total>300):
    print("usted ha ganado una silla ")
    #fin_if

#si el pago que efectuo emmenor que s/.300 se imprme:"siga intentando, se puede llevar una silla"
else:
    print("siga intentando, se puede llevar una silla")
