from random import randint

value_for_comparer=randint(0,9)
for i in range(10):
    if i == value_for_comparer:
        print("los valores son los mismos", i)
print("fin del programa")