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
#vereficador
clientes_regulares=(n_clientes>20)
#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("# EL NUMERO DE CLIENTES ES       :",n_clientes)
print("# COMPRAS AL DIA POR CADA CLIENTE:",compras_por_dia)
print("# EL EFECTIVO QUE SE OBTUVO ES   :",efectivo)
print("###############################")
print("¿Hay una buen acompra?:",clientes_regulares)

#condicional simple
#si el los clientes superan los s/.1000 habra una caja de sorteo
if(efectivo>1000):
    print("felicidades:usted entro al sorteo de una canasta")

#fin_if
