import os
#boleta
#decçlaracion de variables
n_clientes,compras_por_dia=0,0
efectivo=0.0
#input

n_clientes=int(os.sys.argv[1])
compras_por_dia=float(os.sys.argv[2])


#procesing
efectivo=round(n_clientes*compras_por_dia)

#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("# EL NUMERO DE CLIENTES ES       :",n_clientes)
print("# COMPRAS AL DIA POR CADA CLIENTE:",compras_por_dia)
print("# EL EFECTIVO QUE SE OBTUVO ES   :",efectivo)
print("###############################")

#si el los clientes superan los s/.1000 habra una caja de sorteo
#inicio_if
if(efectivo>=100):
    print("felicidades:usted entro al sorteo de una canasta")
#fin_if

#inicio_if
if(efectivo<80):
    print("usted perdio la posibilidad de ganar una canasta")
#fin_if

#inicio_if
if(efectivo>80 and efectivo<100):
    print("casi logra entrar al sorteo de una canasta")
#fin_if
