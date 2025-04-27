###
# Funciones 
# Bloque de código que se puede reutilizar y parametrizar para realizar una tarea específica

import os
os.system("clear")

""" Definicion de una funcion
def nombre_funcion(parametros):
    # bloque de codigo
    return valor_retorno
"""

def saludar():
    print("Hola, soy una funcion")
    return "Hola, soy una funcion"
saludar()

def saludar_persona(nombre: str) -> str:
    print(f"Hola {nombre}, soy una funcion")
    return f"Hola {nombre}, soy una funcion"
saludar_persona("Francisco")
saludar_persona("Jimena")
saludar_persona("Rebeca")
saludar_persona("Javier")



def sumar(a: int, b: int) -> int:
    suma = a + b
    return suma
print(sumar(5, 10))

def restar(a: int, b: int) -> int:
    """ Resta dos numeros y devuelve el resultado"""
    return a - b
print(restar(10, 5))


def multiplicar(a: int, b: int = 2) -> int:
    """ Multiplica dos numeros y devuelve el resultado"""
    return a * b
print(multiplicar(5))


# argumento por clave

def describir_persona(nombre: str, edad: int, sexo: str) -> str:
    """ Describir una persona"""
    print(f"Soy {nombre} tengo {edad} años y soy {sexo}")
    return f"Soy {nombre} tengo {edad} años y soy {sexo}"
""" Los parametros son posicionales"""
describir_persona("Francisco", 36, "hombre")
""" Los argumentos pueden ser pasados por clave"""
describir_persona(edad=36, sexo="hombre", nombre="Francisco ")

# Argumentos de longitud variable

def sumar_varios_numeros(*args: int) -> int:
    """ Sumar varios numeros"""
    suma = 0
    for numero in args:
        suma += numero
    return suma
print(sumar_varios_numeros(1, 2, 3, 4, 6))
print(sumar_varios_numeros(10, -2, 3, 4, -6))
print(sumar_varios_numeros(1, 2, 63, 4, 6))


# Argumento Clave-Valor

def describir_persona_clave_valor(**kwargs: str) -> str:
    """ Describir una persona"""
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
    return str(kwargs)
print(describir_persona_clave_valor(nombre="Francisco", edad="36", sexo="hombre"))
print(describir_persona_clave_valor(nombre="Francisco", edad="36", sexo="hombre", ciudad="Madrid"))