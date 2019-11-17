import os

#boleta
#declaracion de variables
cliente,auriculares,usb,="",0,0
precio_auricular,precio_usb=0.0,0.0

#input
cliente=os.sys.argv[1]
auriculares=int(os.sys.argv[2])
usb=int(os.sys.argv[3])
precio_auricular=float(os.sys.argv[4])
precio_usb=float(os.sys.argv[5])

#procesing
pago_total=precio_auricular*auriculares+precio_usb*usb

#vereficador
cliente_bueno=(pago_total>50)

#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("# el cliente es        :",cliente)
print("# numero auriculares es:",auriculares," precio:",precio_auricular)
print("# numero de usb        :",usb,"         precio:",precio_usb)
print("# pago total           :",pago_total)
print("###############################")
print("¿el cliente invertio ?:",cliente_bueno)

#condicional simple
#si el cliente supera mas de s/.250 se lleba una memoria gratis
if(pago_total>250):
    print("felicidades!!!, usted ha ganado una memoria")
#fin_if
