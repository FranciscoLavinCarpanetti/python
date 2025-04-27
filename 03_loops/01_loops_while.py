###
# Bucles (while)
# Un bucle while ejecuta un bloque de código mientras una condición sea verdadera.
###
import os
os.system("clear")

contador = 0
while contador <= 5:
    print("Contador:", contador)
    contador += 1
# El bucle se detiene cuando la condición ya no es verdadera.

# break
# El bucle se detiene cuando se encuentra una instrucción break.
contador = 0
while contador <= 5:
    print("Contador:", contador)
    if contador == 3:
        break
    contador += 1


# continue

# La instrucción continue salta a la siguiente iteración del bucle.

contador = 0
while contador < 15:
    contador += 1
    if contador % 2 == 0:
        continue
    print("Contador divisible:", contador)
# La instrucción continue salta a la siguiente iteración del bucle.

# bucle else
# El bucle else se ejecuta cuando el bucle while termina su ejecución normalmente.

contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1
else:
    print("El bucle ha terminado.")
# El bucle else se ejecuta cuando el bucle while termina su ejecución normalmente.
# El bucle while se detiene cuando la condición ya no es verdadera.
# El bucle else no se ejecuta si el bucle while se detiene por una instrucción break.


# Pedir información al usuario

numero = -1
while numero < 0:
    try:
        numero = int(input("Introduce un número positivo: "))
        if numero < 0:
          print("El número no es positivo.")
    except ValueError:
        print("El valor introducido no es un número entero.")  
print(f"El número que has introducido es: {numero}")


