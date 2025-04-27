# Secuencia mutable de elementos.
# Pueden tener elementos de diferentes tipos.

import os
os.system("clear")
lista = [1, 2, 3, 4, 5] # Lista de enteros
lista2 =["manzana", "pera", "naranja", "uva"] # Lista de cadenas
#lista3: list[int | str | float | bool]= [1, "manzana", 3.14, True] # Lista de diferentes tipos
lista_vacio = [] # Lista vacía
lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Lista de listas
# Acceso a los elementos de la lista

print(lista)
print(lista2)
print(lista_de_listas)

print(lista[0]) # Primer elemento
print(lista[1]) # Segundo elemento
print(lista[2]) # Tercer elemento
print(lista[3]) # Cuarto elemento


# Slicing 
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(lista1[1:4]) # Primeros 3 elementos
print(lista1[:])
print(lista1[::2]) # Elementos de 2 en 2
print(lista1[::-1]) # Invertir la lista
print(lista1[1:4:2]) # Elementos de 2 en 2

# Modificar elementos de la lista
lista1 += [11, 12, 13, 14, 15] # Concatenar listas
lista1[0] = 100
print(lista1) # [100, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Agregar elementos a la lista
lista1.append(11) # Agregar al final
print(lista1) # [100, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
lista1.insert(0, 0) # Agregar al principio
print(lista1) # [0, 100, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# Eliminar elementos de la lista
lista1.remove(100) # Eliminar el primer elemento que coincida


# Recuperar longitud de la lista
print("LA LONGITUD ES ", len(lista1)) # Longitud de la lista
# Recuperar el índice de un elemento
print(lista1.index(3)) # Índice del elemento 3
# Contar el número de veces que aparece un elemento
print(lista1.count(3)) # Contar el número de veces que aparece el elemento 3

