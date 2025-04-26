#boleanos
# True y False
# se pueden usar para evaluar condiciones sobreto es para comparar 

import os
os.system("clear")

print("operadores de comparacion:")
# True y False
# se pueden usar para evaluar condiciones sobreto es para comparar
print("5 > 3", 5 > 3)
print("5 < 3", 5 < 3)
print("5 == 5", 5 == 5)
print("5 != 3", 5 != 5)  # Example of a meaningful comparison
print("5 >= 5", 5 >= 5)
print("5 <= 3", 5 <= 3)

print("\nEjemplo de cadenas:")
print("manzana < pera", "manzana" < "pera")

print("\nTabla de la verdad:")
print("A     B     A and B")
print("True  True  ", True and True)
print("True  False ", True and False)
print("False True  ", False and True)
print("False False ", False and False)

print("\nA     B     A or B")
print("True  True  ", True or True)
print("True  False ", True or False)
print("False True  ", False or True)
print("False False ", False or False)

print("\nA     not A")
print("True  ", not True)
print("False ", not False)