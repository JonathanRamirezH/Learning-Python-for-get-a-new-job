first_value = eval(input("Ingrese un valor positivo:"))

for i in range(10):
    num = eval(input("Ingrese un valor positivo:"))
    if num > first_value:
        first_value = num
print('el valor mas alto fue:', first_value)