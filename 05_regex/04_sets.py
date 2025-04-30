###
# sets
# Coleccion de elementos unicos
# Se pueden crear de la siguiente manera
# set() o {}
# Se pueden crear a partir de una lista o tupla
# Se pueden crear a partir de un string
# Se pueden crear a partir de un rango

import re

# [: coincide con cualquier caracter dentro de los corchetes]

username = "franci.lavi_88+"
pattern = r"^[\w._%+-]+$"

match = re.search(pattern, username)

if match:  print("El nombre de usuario es válido: ", match.group())
else: print("El nombre de usuario no es válido")


# Ejercicio de busqueda man, fan, ban, ignorando el resto

text = "fan, ran, tsn, ban, san, man, tan, lan, can, dan"
pattern = r"[mfb]an"
matches = re.findall(pattern, text)
print("Palabras encontradas: ", matches)


######
r"[a-zA-Z0-9_]"  # coincide con cualquier letra o número o guion bajo
r"[a-zA-Z0-9_]+"  # coincide con cualquier letra o número o guion bajo, al menos una vez
r"[a-zA-Z0-9_]*"  # coincide con cualquier letra o número o guion bajo, cero o más veces
r"[a-zA-Z0-9_]{3,}"  # coincide con cualquier letra o número o guion bajo, al menos 3 veces
r"[a-zA-Z0-9_]{3,5}"  # coincide con cualquier letra o número o guion bajo, entre 3 y 5 veces
r"[a-zA-Z0-9_]{3,5}?"  # coincide con cualquier letra o número o guion bajo, entre 3 y 5 veces, de forma no codiciosa
r"[a-zA-Z0-9_]{3,5}+"  # coincide con cualquier letra o número o guion bajo, entre 3 y 5 veces, de forma codiciosa
r"[a-zA-Z0-9_]{3,5}*"  # coincide con cualquier letra o número o guion bajo, entre 3 y 5 veces, de forma codiciosa
r"[a-zA-Z0-9_]{3,5}+"  # coincide con cualquier letra o número o guion bajo, entre 3 y 5 veces, de forma codiciosa
####

# [^]: coincide con cualquier caracter que no esté dentro de los corchetes
text = "Hola, soy un texto de prueba"
pattern = r"[^aeiou]"
matches = re.findall(pattern, text)
print("Caracteres encontrados: ", matches)
# [^aeiou]  # coincide con cualquier caracter que no sea una vocal