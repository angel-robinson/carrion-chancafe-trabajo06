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
if(gorras>5):
    print("por su compra se ha ganado una gorra gratis")
#fin_if

#si el cliente compra menos que cinco gorras se imprime:"si lleva dos gorros mas, se lleba una gratis"
#inicio_if
if(gorras<3):
    print("si lleva dos gorros mas, se lleba una gratis")
#fin_if

#si el cliente compra mas de tres polos se imprime:"llevese un polo gratis"
#inicio_if
if(polos>3):
    print("llevese un polo gratis")
#fin_if
