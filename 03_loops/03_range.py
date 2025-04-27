###
# Range 
# Permite de crear una secuencia de números enteros
# Se puede usar en un bucle for
# Se puede usar en un bucle while
# Se puede usar en una lista
# Se puede usar en un diccionario
# Se puede usar en una tupla
# Se puede usar en un conjunto
# Se puede usar en un string

import os
os.system("clear")


for nums in range(10):
    print(nums)

for nums in range(0, 10, 2):
    print(nums)



for nums in range(0, 456):
    print(nums)


# Lista
nums = range(0, 10)
list_of_nums = list(nums)
print(list_of_nums)


for _ in range(10):
    print("Hola")
  
