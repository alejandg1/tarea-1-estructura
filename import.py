#################       import                      ###################
## importando por completo el modulo math e imprimiendo raiz cuadrada de 2 usando el modulo importado
import math

print(math.sqrt(4))  ###>>>>>  2.0
print("---------------------------------------------------------------")
## importando modulo bajo un alias

import math as mth

print(mth.sqrt(4))  ##>>>>  2.0
print("---------------------------------------------------------------")

## importar funciones especificas desde un modulo

from math import sqrt

print(sqrt(16))  ##>>>> 4.0
print("---------------------------------------------------------------")


############################################################################################


#########################      break, continue     ############################
print("continue/break---------------")

## salir de un bucle cuando se halle un valor especifico
Listl = ["Ana", "Sam", "Dany", "Diana", "Ale"]
for nombre in Listl:
    if nombre == "Diana":
        print(nombre, "Encontrada")
        break

print("---------------------------------------------------------------")
## ignorar valores dentro de un bucle para imprimir solo números pares
Listl2 = [1, 2, 3, 4, 5, 6, 7, 8]
for num in Listl2:
    if (num % 2) != 0:
        continue
    else:
        print(num)

print("---------------------------------------------------------------")

## salir de un bucle while al cumplirse una condición


Ln_value = 0
while Ln_value < 20:
    if Ln_value == 11:
        break
    else:
        Ln_value += 1
    print(Ln_value)

print("---------------------------------------------------------------")

## salir de bucles anidados cuando se cumpla una condición

for Ln_count in range(5):
    for Ln_count2 in range(5):
        if Ln_count > Ln_count2:
            break
        print(Ln_count, "-", Ln_count2)

print("---------------------------------------------------------------")

## ignorar valores dentro de un bucle while

Ln_val = 0
while Ln_val < 20:
    Ln_val += 1
    if (Ln_val % 2) == 0:
        continue
    print(Ln_val)

print("---------------------------------------------------------------")

print()

####################################################################################
