
###
# Meta caracteres 
# Los metacaracteres son caracteres especiales que tienen un significado particular en las expresiones regulares.
# Se utilizan para definir patrones de búsqueda más complejos.
# Algunos de los metacaracteres más comunes son:
# .  -> Coincide con cualquier carácter excepto un salto de línea.
# ^  -> Coincide con el inicio de una línea.
# $  -> Coincide con el final de una línea.
###

import re

# el punto (.) coincide con cualquier carácter excepto un salto de línea

text = "Hola mundo, HOla de nuevo", "H0la ota vez", "h!la por ultima vez"
pattern = "H.la"  # Coincide con "Hola", "H0la", "Hala", etc.

found = re.findall(pattern, text)

if (found):
 print(found)
else:
 print("No se encontraron coincidencias")

 

 text = "Mi casa es azul. Y el coche es rojo."
 pattern = r"\."
 matches = re.findall(pattern, text)
 print(matches)  # Coincide con el punto (.) en la cadena

 # /d: Coincide con cualquier dígito (0-9)

text = "Mi número de teléfono es 1234567890."
pattern = r"\d{9}"  # Coincide con cualquier dígito
matches = re.findall(pattern, text)
print(matches)  # Coincide con los dígitos en la cadena

# Ejercicio: detectar números de teléfono españa

text = "Mi número de teléfono es +34 123456789 quieres guardarlo."
pattern = r"\+34 \d{9}"  # Coincide con el número de teléfono
matches = re.search(pattern, text)
if matches: print(f"Número de teléfono encontrado: {matches.group()}")
else: print("No se encontró ningún número de teléfono.")

# \w: Coincide con cualquier carácter alfanumérico (letras y dígitos) y el guion bajo (_)

text = "Hola_mundo123"
pattern = r"\w"  # Coincide con cualquier carácter alfanumérico
matches = re.findall(pattern, text)
print(matches)  # Coincide con "Hola_mundo123"

# \s: Coincide con cualquier carácter de espacio en blanco (espacio, tabulación, salto de línea)

text = "Hola mundo\nHola de nuevo"
pattern = r"\s"  # Coincide con cualquier carácter de espacio en blanco
matches = re.findall(pattern, text)
print(matches)  # Coincide con los espacios y saltos de línea en la cadena

# ^: Coincide con el inicio de una línea/cadena

username = "@123_Hola" # Nombre de usuario no válido por el símbolo @
pattern = r"^\w"  # Coincide con cualquier carácter alfanumérico al inicio de la cadena
valid = re.search(pattern, username)
if valid: print("El nombre de usuario es válido")
else: print("El nombre de usuario no es válido")

# $: Coincide con el final de una línea/cadena

text = "Hola mundo"
pattern = r"mundo$"  # Coincide con "mundo" al final de la cadena
matches = re.search(pattern, text)
if matches: print("Coincidencia encontrada")
else: print("No se encontró coincidencia")

# \b: Coincide con un límite de palabra (inicio o final de una palabra)

text = "Hola mundo, Hola de nuevo"
pattern = r"\bHola\b"  # Coincide con "Hola" como una palabra completa
matches = re.findall(pattern, text)
if matches: print("Coincidencia encontrada")
else: print("No se encontró coincidencia")

# Ejercicio: detertar final de correo electrónico basico

text="fra@gmail.com"
pattern = r"^+w@gmail.com"  # Coincide con el dominio de Gmail
matches = re.search(pattern, text)
if matches: print("Coincidencia con el final, dominio de Gmail")
else: print("No se encontró coincidencia")

# /b: Coincide con un límite de palabra (inicio o final de una palabra)

text = "casa casado casada"
pattern = r"\bcasa\b"  # Coincide con "casa" como una palabra completa
matches = re.findall(pattern, text)
if matches: print("Coincidencia encontrada")
else: print("No se encontró coincidencia")

# |: Coincide con una alternativa (OR)

text = "platano, manzana, naranja, banana"
pattern = r"platano|banana"  # Coincide con "platano" o "manzana"
matches = re.findall(pattern, text)
print(matches)  # Coincide con "platano" o "banana"

