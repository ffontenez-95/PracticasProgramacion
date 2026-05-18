"""
Crear una función que permita ingresar números romanos por teclado. 
La carga de datos cuando se ingrese el número romano M. 
    a. ¿Cuántos números fueron iguales a 5 en números romanos? 
    b. ¿Cuántos números fueron iguales a 30 en números romanos? 
    c. ¿Cuántos números fueron iguales a 90 en números romanos? 
    d. ¿Cuántos números fueron iguales a 100 en números romanos? 
"""

def ingrese_nro_romanos ():
    """
    Esta funcion calcula cuantas veces el usuario ingresa numeros romanos
    sale del bucle cuando el usuario aprieta M
    I=1     V=5     X=10     L=50     C=100     D=500
    """
    contador_5=0
    contador_30=0
    contador_90=0
    contador_100=0

    while True:
        
        numero_romano= (input("Ingrese numeros romanos\n")).lower()

        if numero_romano == "m":
            break

        #Asignamos valores a los contadores

        if numero_romano == "v":
            contador_5+=1

        elif numero_romano == "xxx":
            contador_30+=1
        
        elif numero_romano == "xc":
            contador_90+=1
        
        elif numero_romano == "c":
            contador_100+=1


    print (f"Usted ingreso la cantidad de {contador_5} que dan como resultado 5 en numeros romanos")   
    print (f"Usted ingreso la cantidad de {contador_30} que dan como resultado 30 en numeros romanos")
    print (f"Usted ingreso la cantidad de {contador_90} que dan como resultado 90 en numeros romanos")
    print (f"Usted ingreso la cantidad de {contador_100} que dan como resultado 100 en numeros romanos")


ingrese_nro_romanos()