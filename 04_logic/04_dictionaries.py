###
# Los diccionarios son estructuras de datos que almacenan pares clave-valor.
# Se definen con llaves {} y los pares clave-valor se separan por comas.
# Las claves deben ser únicas y pueden ser de cualquier tipo inmutable (números, cadenas, tuplas).
# Los valores pueden ser de cualquier tipo.

persona = {
    "nombre": "Francisco",
    "apellido": "Lavin",
    "estado_civil": "Casado",
    "edad": 36,
    "ciudad": "Madrid",
    "deportes": {
        "futbol": True,
        "tenis": False,
        "baloncesto": False,
        "rugby": True
    }
}
print(persona["apellido"])
print(persona["deportes"]["futbol"])

#Cambaiur el valor de una clave

persona["edad"] = 37
print(persona["edad"])

# Eliminar completamente una clave
del persona["ciudad"]
print(persona)

estado_civil = persona.pop("estado_civil")
print(f"Estado civil: {estado_civil}")
print(persona)

# Sobreescribir un valor con otro dicicionario
a = {"nombre": "Francisco", "apellido": "Lavin"}
b = {"nombre": "Javier", "apellido": "Carpantier", "es_estudiante": True}

a.update(b)
print(a)

# Comprobar si existe una clave en el diccionario
print("nombre" in a)  # True
print("ciudad" in a)  # False

# Para optener todas las claves de un diccionario, se puede usar el método keys()
print(a.keys())  # dict_keys(['nombre', 'apellido', 'es_estudiante'])

# Para obtener todos los valores de un diccionario, se puede usar el método values()
print(a.values())  # dict_values(['Javier', 'Carpantier', True])

# Para ontener clave como valor, se puede usar el método items()
print(a.items())  # dict_items([('nombre', 'Javier'), ('apellido', 'Carpantier'), ('es_estudiante', True)])


