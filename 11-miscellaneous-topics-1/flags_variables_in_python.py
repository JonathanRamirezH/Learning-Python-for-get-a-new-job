from random import randint

flag_variable=0
limit_variable=randint(1,20)

print(limit_variable)
for i in range(2,limit_variable):
    if (limit_variable % i )== 0:
        flag_variable=1
if flag_variable == 1:
    print("No es un numero primo")
else:
    print("Es un numero primo")