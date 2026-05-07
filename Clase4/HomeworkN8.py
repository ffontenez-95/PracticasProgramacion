"""
Una empresa de transporte ofrece su servicio para enviar paquetes a tres provincias de la Patagonia Argentina. 

Cuando un cliente quiere enviar un paquete, puede elegir por distintos tipos de pesos Ej: (paquete de 15 kg a 20 kg).  El cliente contrata el servicio de transporte eligiendo una provincia como destino y un peso de paquete. 

Se necesita realizar un algoritmo para saber el precio final a pagar. 

En la siguiente tabla se muestran los destinos con cada peso admitido y su precio correspondiente.

SANTA CRUZ: 
MENOR A 5KG: $200
ENTRE 6 Y 10KG: $300
ENTRE 11 Y 20KG: $400

CHUBUT:
MENOR A 5KG: $350
ENTRE 6 Y 10KG: $390
ENTRE 11 Y 20KG: $420

RIO NEGRO:
MENOR A 5KG: $400
ENTRE 6 Y 10KG: $480
ENTRE 11 Y 20KG: $510

"""
print ("---EMPRESA DE TRANSPORTE---")

#Preguntamos a donde va a ser el envio
destino=input("Bienvenido, a donde quiere realizar el envio. ¿Santa Cruz, Chubut o Rio Negro?\n").lower()

print(f"Elegiste: {destino}")

peso= """
Seleccione la opcion 1, 2 o 3 segun el peso que corresponda:

1= Menor a 5 kg
2= Entre 6 kg y 10 kg
3= Entre 11 y 20kg

"""

opcion= int(input(peso))

# SANTA CRUZ
if destino == "santa cruz" and opcion == 1:
    print (f" Su envio es menor a 5kg, debe abonar $200")
    
elif destino == "santa cruz"and opcion == 2:
        print (f" Su envio es entre 6 kg y 10 kg, debe abonar $300")
    
elif destino == "santa cruz"and opcion ==3:
        print (f" Su envio es entre 11 kg y 20 kg, debe abonar $400")    

# CHUBUT
if destino == "chubut" and opcion == 1:
    print (f" Su envio es menor a 5kg, debe abonar $350")
elif destino == "chubut" and opcion == 2:
      print (f" Su envio es entre 6 kg y 10 kg, debe abonar $390")
    
elif destino == "chubut" and opcion ==3:
        print (f" Su envio es entre 11 kg y 20 kg, debe abonar $420")    

# RIO NEGRO
if destino == "rio negro" and opcion == 1:
        print (f" Su envio es menor a 5kg, debe abonar $400")
    
elif destino == "rio negro" and opcion == 2:
        print (f" Su envio es entre 6 kg y 10 kg, debe abonar $480")
    
elif destino == "rio negro" and opcion ==3:
        print (f" Su envio es entre 11 kg y 20 kg, debe abonar $510")   

else:
        print (" Seleccione las opciones correctas")
