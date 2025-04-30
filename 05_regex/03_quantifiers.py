###
# Quantificadores
# Los cuantificadores son caracteres especiales que indican la cantidad de veces que un patrón debe aparecer en una cadena.
# Los cuantificadores más comunes son:
# * (cero o más veces)
# + (una o más veces)
# ? (cero o una vez)
# {n} (exactamente n veces)
# {n,} (n o más veces)
# {n,m} (entre n y m veces)
# Los cuantificadores se pueden combinar con otros patrones para crear expresiones regulares más complejas.

import re

# * (cero o más veces)
text = "abbbbc"
pattern = "a*"
match = re.findall(pattern, text)
print(match)

# + (una o más veces)
text = "abb bbc abbbabc"
pattern = "a+"
matches = re.findall(pattern, text)
print(matches)

# {n} (exactamente n veces)

text = "abbbaabaaaac"
pattern = "b{4}"
match = re.findall(pattern, text)
print(match)


# {n, m} (entre n y m veces)

text = "a aaa  aaa  aa aaaaaa aaaa a aaa"
pattern = r"\w{2,4}"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio: encuentra todas las palabras que tengan entre 4 y 6 letras

text = "Hola, soy un texto con palabras de diferentes longitudes."
pattern = r"\b\w{4,6}\b"
matches = re.findall(pattern, text)
print(matches)

text = "Hola, soy un texto con palabras de diferentes longitudes."
pattern = r"\b\w{6,}\b" # Palabras con 6 o más letras
matches = re.findall(pattern, text)
print(matches)
