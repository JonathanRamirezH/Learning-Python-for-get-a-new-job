'''Hacer uso de if cada que hacemos condiciones, puede resultar malo, 
puesto que al usarlo siempre lo que genera es que se ejecuten todos los 
bloques de codigo, sin restriccion alguna provocando un menor rendimiento
en el programa, es por tal motivo que existe ELIF dentro de Python'''
valor_a_comparar=20
if valor_a_comparar < 21:
    print("Es menor a 21")
if valor_a_comparar<22:
    print("Es menor a 22")
if valor_a_comparar == 20:
    print("Son valores iguales")

#El objetivo del ELIF es solamente ejecutar un bloque de codigo con el cual
#la condicion se cumpla.
if valor_a_comparar > 25:
    print("El valor es menor a 25 condicion con ELIF")
elif valor_a_comparar > 15:
    print("El valor es mayor a 15 condicion con ELIF")
elif valor_a_comparar == 20:
    print("los valores son iguales condificion con ELIF")