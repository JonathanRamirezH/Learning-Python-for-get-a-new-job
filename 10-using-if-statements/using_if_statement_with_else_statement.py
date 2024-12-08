from random import randint

value_input = eval(input("ingrese un numero del 1 al 9\n"))
value_random= randint(0,9)
if value_input == value_random:
    print("Acertaste!!")
else:
    print("Vuelve a intentar,el resultado era:", value_random)