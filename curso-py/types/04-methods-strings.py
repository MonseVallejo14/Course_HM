spoiled = "  murphy bebe  "
print(spoiled.upper())  # Todas mayúsculas
print(spoiled.lower())  # Todas minúsculas
print(spoiled.lstrip().capitalize())  # La primera mayúscula
print(spoiled.title())  # La pirmera de lcad letra mayúscula
print(spoiled.strip())  # Quila los espacioa a ambos lados
print(spoiled.lstrip())  # Quita los espacios a la izquierda
print(spoiled.rstrip())  # Quita los espacios a la derecha
print(spoiled.find("ph"))  # Busca lo qeu se le indique en el string
# Reemplaza lo que se le indique en el string
print(spoiled.replace("ph", "f").replace("u", "o"))
print("rph" in spoiled)  # Verifica si lo que se pide está en el string
print("rph" not in spoiled)
# Verifica si lo que se le pide NO está en el string
