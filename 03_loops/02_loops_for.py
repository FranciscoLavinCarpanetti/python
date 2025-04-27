###
# bucle for
# El bucle for se utiliza para iterar sobre una secuencia (lista, tupla, diccionario, conjunto o cadena).
# Se puede usar la función range() para generar una secuencia de números.
# Ejemplo 1: Iterar sobre una lista
# Ejemplo 2: Iterar sobre una cadena
# Ejemplo 3: Iterar sobre un diccionario
# Ejemplo 4: Iterar sobre un conjunto
# Ejemplo 5: Usar la función range() para generar una secuencia de números

import os
os.system("clear")


frutas = ["manzana", "banana", "cereza", "naranja", "uva", "kiwi"]
for fruta in frutas:
    print(fruta)

#iterar sobre una cadena
cadena = "Francisco"
for letra in cadena:
    print(letra)


# enumerate() devuelve un objeto enumerado.

frutas = ["manzana", "banana", "cereza", "naranja", "uva", "kiwi"]
for index, fruta in enumerate(frutas):
    print(index, fruta)


# bucle anidado

letras = ["a", "b", "c", "d", "e"]
numeros = [1, 2, 3, 4, 5]

for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")


#break y continue


animales = ["perro", "gato", "elefante", "jirafa", "león"]
for idx, animal in enumerate(animales):
    print(animal)
    if animal == "elefante": 
      print(f"el elefante es el {idx + 1}° animal")
      break

#continue

animales = ["perro", "gato", "elefante", "jirafa", "león"]
for idx, animal in enumerate(animales):
    if animal == "elefante": 
      continue
    print(animal)    

# Listas comprensivas
# Se pueden usar bucles for para crear listas comprensivas.


anuncios = ["Hola", "Adiós", "Buenos días", "Buenas tardes", "Buenas noches"]
anuncios_mayusculas = [anuncio.upper() for anuncio in anuncios]
print(anuncios_mayusculas)

# muestra numeros pares

pares =[num for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if num % 2 == 0]
print(pares)



