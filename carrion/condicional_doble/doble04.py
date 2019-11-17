import os
#boleta d venta
#declaracion de variables
pasajero,numero_de_pasajes,precio_pasaje="",0,0.0

#input
pasajero=os.sys.argv[1]
numero_de_pasajes=int(os.sys.argv[2])
precio_pasaje=float(os.sys.argv[3])

#procesimg
costo_pasajero=round(numero_de_pasajes*precio_pasaje)

#vereficador
costo_excesivo=(costo_pasajero>=200)

#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("#PASAJERO          :",pasajero)
print("# PRECIO DEL PASAJE:",precio_pasaje)
print("COSTO POR PASJERO  :",costo_pasajero)
print("###############################")
print("¿EL COSTO ES EXCESIVO?:",costo_excesivo)

#condicional doble
#el comprador ha ganado un pasaje vip
#inicio_if
if(costo_pasajero>500):
    print("felicidades!!!; ha ganado un pasaje vip")
#fin_if

#si el clienteno supera el total de s/.500 se imprime:"gracias por viajar con nosotros, vuelva pronto"
else:
    print("gracias por viajar con nosotros, vuelva pronto")
