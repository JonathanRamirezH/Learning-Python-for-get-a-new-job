x=10
y=20
print("Valor de x:", x, "\nValor de y:", y)
print()

#INTERCAMBIO DE VALORES
x = y 
y = x
print("Valor de x:", x, "\nValor de y:", y)
#No se conserva el valor de x para el proceso de intercambio de valores
#Nota: para seguir manteniendo el valor de un a varibles se hace uso de una
#tercera variblea para contenerla.
a = 15
b = 10
hold_variable=0
print("Valor de a:", a, "\nValor de b:", b)
print()
hold_variable=a
a=b
b=hold_variable
print("Valor de a:", a, "\nValor de b:", b)
print()
#Truco dentro de Python
#primer_variable,segunda_variable = segunda_variable,primer_variable
c=5
d=10
print("Valor de c:", c, "\nValor de d:", d)
c,d = d,c
print("Valor de c:", c, "\nValor de d:", d)