import os

#boleta  de venta
#eclaracion de variables
nombre,cantidad_docenas,precio_docena="",0,0.0

#INPUT
nombre=os.sys.argv[1]
cantidad_docena=int(os.sys.argv[2])
precio_docena=float(os.sys.argv[3])

#PROCESSING
precio_total=round(cantidad_docenas*precio_docena)

#VERIFICADOR
beneficia_la_compra=(precio_total==80)

#OUTPUT
print("###########################")
print("# BOLETA DE VENTA")
print("###########################")
print("#")
print("# nombre    :",nombre)
print("# cantidad  :",cantidad_docenas)
print("# valor     :s/",precio_docena)
print("total       :s/",precio_total)
print("###########################")
print("¿la compra es beneficiosa?",beneficia_la_compra)

#condicional multiple
#el cliente se gana una docena
#inicio_if
if(precio_total>1000):
    print("sorpresa!!!, se puede llevar gratis una docena")
#fin_if

#si el precio es mayor que s/.500 se imprime:"usted ha ganodo medio producto gratis"
#inicio_if
if(precio_total>500):
    print("usted ha ganodo medio producto gratis")
#fin_if

#si el precio total es menor que s/.500 se imprime:"vuelva pronto,gracias"
#inicio_if
if(precio_total<500):
    print("vuelva pronto,gracias")
#fin_if
