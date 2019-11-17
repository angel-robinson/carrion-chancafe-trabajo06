import os

#boleta
#declaracion de variables

nombre,numero_lapiceros,precio_lapiceros="",0,0.0
pago_total=0.0

#input
nombre=os.sys.argv[1]
numero_lapiceros=int(os.sys.argv[2])
precio_lapiceros=float(os.sys.argv[3])

#procesing
pago_total=round(precio_lapiceros*numero_lapiceros)

#vereficador
cantidad=(numero_lapiceros>10)

#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("# el cliente es            :",nombre)
print("# numero total de lapiceros:",numero_lapiceros)
print("# precio de cada lapicero  :",precio_lapiceros)
print("# pago total               :",pago_total)
print("###############################")
print("¿invierte regular en lapiceros ?:",cantidad)

#condicional simple
#si el cliente lleba un total mayor o igual que s/.50 se lleba una caja de lapiceros gratis
if(pago_total>=50):
    print("usted ha ganado una caja de lapiceros pilot gratis")
#fin_if
