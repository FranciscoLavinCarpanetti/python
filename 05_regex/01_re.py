###
# Expreciones regulares
# Patrón de búsqueda
# Se utiliza para buscar patrones en cadenas de texto
# Se utiliza para validar cadenas de texto
# Se utiliza para extraer información de cadenas de texto
# Se utiliza para reemplazar información en cadenas de texto
# Se utiliza para dividir cadenas de texto
# Se utiliza para buscar y reemplazar información en cadenas de texto

# Importar el módulo re
import re

# Crear un patron de texto
pattern = "Francisco"

# El texto dodne se va a buscar el patron
text = "Hola Francisco, como estas? Hola Francisco, como estas? Hola Francisco, como estas?"

# Usar la funcion search para buscar el patron en el texto
result = re.search(pattern, text)

if result:
    print("El patron fue encontrado en el texto")
else:
    print("El patron no fue encontrado en el texto")

print(result.group())  # Imprime el texto encontrado

print(result.start())  # Imprime la posicion donde se encontro el patron

print(result.end())  # Imprime la posicion donde termina el patron

print(result.span())  # Imprime la posicion donde se encontro el patron


# Otro  ejemplo

text = "Los programadores son los que programan numerosas aplicaciones en diferentes lenguajes de programación pero se sienten amenazados por la IA"
pattern = "pero"
found_ia = re.search(pattern, text)

if found_ia:
    print(f"He encontrado el patron en el texto en la posision {found_ia.start()} y termina en la posicion {found_ia.end()}")
else:   
    print("No he encontrado el patron en el texto")


###
# Encontrar todas las coincidencias de un patron en un texto

text = "Me gista python, me gusta python, me gusta python"
pattern = "python"
found_python = re.findall(pattern, text)
print(f"He encontrado el patron {pattern} en el texto {found_python}")
print(len(found_python))  # Imprime la cantidad de veces que se encontro el patron

# metodo iter() para encontrar todas las coincidencias de un patron en un texto
text = "Me gista python, me gusta python, me gusta python"
pattern = "python"
found_python = re.finditer(pattern, text)
for match in found_python:
    print(found_python.group(), found_python.start(), found_python.end())  # Imprime el texto encontrado
    
 #  Modificadores

text = "Los programadores son Ia los que programan numerosas aplicaciones en diferentes lenguajes de ia programación pero se sienten amenazados por la IA"
pattern = "pero"
found_ia = re.findall(pattern, text, re.IGNORECASE)

if found_ia:
    print(f"He encontrado el patron en el texto en la posision {found_ia.start()} y termina en la posicion {found_ia.end()}")
else:   
    print("No he encontrado el patron en el texto")

if found_ia:
    print(found_ia)



 # sub() para reemplazar un patron en un texto

text = "Me gusta python, me gusta python, me gusta python"
pattern = "python"
replacement = "java"
new_text = re.sub(pattern, replacement, text)
print(new_text)  # Imprime el texto con el patron reemplazado