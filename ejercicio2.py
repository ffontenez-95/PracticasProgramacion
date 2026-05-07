"""
Supermercado
Si el cliente compra más de $10.000, obtiene un 10% de descuento. Consigna: Pedir el monto de la compra y calcular el precio final.
"""

print ("---CALCULO DE DESCUENTOS")

#pedimos al cliente el monto de la compra:

compra= float(input("Ingrese el monto total de su compra: "))

if compra >= 10000:
    print ("Tu compra supera la compra minima, tenes un 10% de descuento. El monto a pagar es de: ", compra*0.9 , "$.")

elif compra > 0 and compra <10000:
    print ("No alcanzas el monto minimo, para obtener un descuento. Debes abonar: ", compra , "$." )

else:
    print ("No puede ingresar un valor negativo")