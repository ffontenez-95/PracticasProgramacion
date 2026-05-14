"""Crear una función que calcule el IVA de un producto y lo imprima con la leyenda 
“El IVA correspondiente al (valor ingresado) es (resultado de la función)."""


def calculador_iva(producto):
    """
    Funcion para calcular el iva de un producto
    Se recibe un parametro y el return hace el calculo de IVA del producto
    """
    
    iva=0.21
    return  producto * iva

#Definimos el valor de la variable
producto= 100
 
#Creamos variable para la funcion 
resultado_iva= calculador_iva(producto)

#Imprimimos el mensaje con las variables
print (f"El IVA correspondiente al {producto} es {resultado_iva}")