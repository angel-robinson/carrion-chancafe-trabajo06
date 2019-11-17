import os
#boleta
#declaracion de variables
numero_productos,p_producto1,p_producto2=0,0.0,0.0

#input
numero_productos=int(os.sys.argv[1])
p_producto1=float(os.sys.argv[2])
p_producto2=float(os.sys.argv[3])
#procesing
total=(p_producto1+p_producto2)*numero_productos
#vereficador
ganancia_adecuada=(total>100)
# OUTPUT
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("# EL NUMERO DE CLIENTES ES        :",numero_productos)
print("# EL PRECIO DEL PRIMER PRODUCTO ES:",p_producto1)
print("# PRECIO DEL SEGUNDO PRODUCTO ES  :",p_producto2)
print("# GANANCIA TOTAL                  :",total)
print("###############################")
print("¿HAY UNA GANANCIA ADECUADA?:",ganancia_adecuada)
#si el cliente lleba en compras mas de 100 se lleba un productomenor de s/.5
#inicio_if
if(total>80):
    print("felicidades ha ganado un producto menor que s/.5 totalmente gratis")
#fin_if

#si el cliente nosupera el monto de s/.80 se imprime :"gracias por su visita,vuelva pronto"
else:
    print("gracias por su visita,vuelva pronto")
