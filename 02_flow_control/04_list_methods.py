import os
os.system("clear")
# # Métodos de listas
# # append() Agregar un elemento al final de la lista
# # extend() Agregar varios elementos al final de la lista
# # insert() Agregar un elemento en una posición específica
# # remove() Eliminar el primer elemento que coincida
# # pop() Eliminar el último elemento de la lista y devolverlo
# # clear() Eliminar todos los elementos de la lista
# # index() Devolver el índice del primer elemento que coincida
# # count() Contar el número de veces que aparece un elemento
# # sort() Ordenar la lista
# # reverse() Invertir el orden de los elementos de la lista
# # copy() Devolver una copia de la lista
# # join() Unir los elementos de la lista en una cadena
# # split() Dividir una cadena en una lista
# # list() Convertir un iterable en una lista
# # all() Devolver True si todos los elementos de la lista son verdaderos
# # any() Devolver True si al menos un elemento de la lista es verdadero
# # sum() Devolver la suma de los elementos de la lista
# # min() Devolver el elemento mínimo de la lista
# # max() Devolver el elemento máximo de la lista
# # sorted() Devolver una lista ordenada
# # reversed() Devolver una lista invertida
# # zip() Unir dos o más listas en una lista de tuplas
# # enumerate() Devolver una lista de tuplas con el índice y el elemento
# # filter() Filtrar los elementos de una lista
# # map() Aplicar una función a los elementos de una lista
# # reduce() Aplicar una función a los elementos de una lista y devolver un solo valor
# # all() Devolver True si todos los elementos de la lista son verdaderos
# # any() Devolver True si al menos un elemento de la lista es verdadero
# # list comprehension Crear una lista a partir de otra lista   
# # generator expression Crear un generador a partir de una lista


lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista1.append(11) # Agregar al final
print(lista1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

lista1.extend([12, 13, 14, 15]) # Agregar varios elementos al final
print(lista1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

lista1.insert(1, 100) # Agregar al principio
print(lista1) # [1, 100, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

lista1.extend([16, 17, 18, 19, 20]) # Agregar varios elementos al final
print(lista1) # [1, 100, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

lista1.remove(100) # Eliminar el primer elemento que coincida
print(lista1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

lista1.pop(3) # Eliminar el cuarto elemento
print(lista1) # [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

lista1.clear() # Eliminar todos los elementos de la lista


#metodos mas utiles

numeros = [12, 2, 53, 14, 56, 36, 77, 48, 9, 110]
numeros.sort() # Ordenar la lista
print(numeros) # [2, 9, 12, 14, 36, 48, 53, 56, 77, 110]

numeros = [12, 2, 53, 14, 56, 36, 77, 48, 9, 110]
sorted_numeros = sorted(numeros) # Ordenar la lista
print(sorted_numeros) # [2, 9, 12, 14, 36, 48, 53, 56, 77, 110]


print("ordenar una lista de cadenas de texto (mesclado mayusculas y minusculas)")

nombres = ["juan", "Pedro", "Maria", "ana", "Luis", "Carlos", "Jorge", "marta", "Laura", "sofia"]
nombres.sort(key=str.lower) # Ordenar la lista ignorando mayusculas y minusculas
print(nombres) # ['ana', 'Carlos', 'Jorge', 'Juan', 'Laura', 'Luis', 'Maria', 'marta', 'Pedro', 'sofia']


animales = ["perro", "gato", "elefante", "jirafa", "león", "tigre", "oso", "leon", "gato", "gallo"]

print(len(animales)) # Longitud de la lista
print(animales.count("gato")) # Contar el número de veces que aparece el elemento "gato"
print("gallo" in animales) # Comprobar si el elemento "gallo" está en la lista


