variable_for_count=0
decenas_contador =0
for i in range(100):
    variable_for_count+=1
    print(variable_for_count)
    if (variable_for_count % 10) == 0:
        decenas_contador+=1
print('fin del programa')
print('valor hasta al que se llego:', variable_for_count)
print('Decenas encontradas:', decenas_contador)