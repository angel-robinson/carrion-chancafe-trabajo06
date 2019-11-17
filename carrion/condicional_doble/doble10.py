import os
#boleta
#declaracion de variables
cliente,gorras,polos="",0,0
precio_gorras,precio_polos=0.0,0.0
#input
cliente=os.sys.argv[1]
gorras=int(os.sys.argv[2])
precio_gorras=float(os.sys.argv[3])
polos=int(os.sys.argv[4])
precio_polos=float(os.sys.argv[5])
#procesing
pago_total=(precio_gorras*gorras+precio_polos*polos)
#vereficador
cliente_procutos=(polos+gorras>5)
#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("# el cliente es     :",cliente)
print("# numero gorras es  :",gorras," precio:s/.",precio_gorras)
print("# numero de polos es:",polos," precio:s/.",precio_polos)
print("# pago total        :",pago_total)
print("###############################")
print("¿llevo mas que cinco productos?:",cliente_procutos)
#si el cliente lleva 3 gorras se lleva una gratis
#inicio_if
if(gorras>3):
    print("por su compra se ha ganado una gorra gratis")
#fin_if

#si el cliente no supero la compra,se imprime:"si compra tres gorras se puede llevar una gratis"
else:
    print("si compra tres gorras se puede llevar una gratis")
