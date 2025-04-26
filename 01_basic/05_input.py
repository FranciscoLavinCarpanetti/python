
estado = input("Hola, ¿cómo estás?\n")
print(f"saber que estás " + estado + " me interesa")

age = input("¿Cuántos años tienes?\n")
age = int(age)
print(f"Me alegra saber que tienes {age} años")

print("obtener multiples valores a la vez")
country, city = input("¿De qué país y ciudad eres?\n").split(", ")
print(f"Me alegra saber que eres de {city} en {country}")