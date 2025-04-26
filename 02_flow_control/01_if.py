###
# sentencia condicional (if, elif, else)
# permiten ejecutar un bloque de código si se cumple una condición
###

import os
os.system("clear") # import os y limpiar la consola

edad = 18
if edad >= 18:
 print("Eres mayor de edad") # se ejecuta si la condición es verdadera dentro del bloque if ()


 edad = 17
if edad >= 18:
 print("Eres mayor de edad") # no se ejecuta si la condición es falsa dentro del bloque if ()
else:
 print("Eres menor de edad") # se ejecuta si la condición es falsa dentro del bloque else ()

# se puede usar elif para agregar más condiciones

nota = 7
if nota >= 9:
 print("Excelente")
elif nota >= 7:
 print("Buena")
elif nota >= 5:
 print("Regular")
elif nota >= 3:
 print("Mala")  
else:
    print("¡no estas calificado!") # se ejecuta si la condición es falsa dentro del bloque else ()


# Condiciones multiples
# se pueden usar operadores logicos para combinar condiciones
# and: ambas condiciones deben ser verdaderas
# or: al menos una de las condiciones debe ser verdadera
# not: invierte el valor de la condición
edad = 18
if edad >= 18 and edad < 65:
 print("Eres adulto")
elif edad >= 65:
 print("Eres adulto mayor")
else:
 print("Eres menor de edad")

carnet_conducir = True

if edad >= 18 or carnet_conducir:
    print("Puedes conducir")
else:
    print("No puedes conducir")


es_fin_de_semana = True
if not es_fin_de_semana:
    print("Puedes descansar")   

edad =18
tiene_dinero = True
if edad >= 14:
  if tiene_dinero:
      print("Puedes comprar alcohol")
  else:
        print("No puedes comprar alcohol")
else:
    print("No puedes comprar alcohol")   

#cuidado con el anidado de condiciones
# se recomienda usar funciones para evitar el anidado de condiciones


numero = 5
if numero: # true
    print("El numero no es cero")

numero = 0
if numero: # false
    print("Aqui no entrara nunca")

numero = ""
if numero: 
    print("El numero no es vacio")

numero = 3
es_el_tres = numero == 3
if es_el_tres:
    print("El numero es 3")
  
     
print("La condicion Ternaria")     
# se puede usar una sola linea para evaluar una condicion if-else 

edad = 17

mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(mensaje) # se ejecuta si la condición es verdadera dentro del bloque if ()
# se ejecuta si la condición es falsa dentro del bloque else ()
# se puede usar una sola linea para evaluar una condicion if-else
