# Crear un diccionario
estudiante = {"nombre": "Everardo", "Curso": "Fundamentos de Python"}
print(estudiante)

#Actualizando un diccionario
estudiante["nombre"] = "Angloamerican"
print(str(estudiante))

"""print(estudiante)

estudiante.pop("Curso")
print(estudiante)

paises = {}
# Agregando elementos al diccionario
paises["MEX"] = "Mexico"
paises["COL"] = "Colombia"
paises["CHL"] = "Chile"
print(paises)

if "CRI" in paises:  # Preguntamos si existe la clave en el diccionario
    print("¿Deseas reemplazar el valor?")
    paises["CRI"] = input()
else:  # No existe esa clave
    paises["CRI"] = "Costa Rica"
    print(paises)

# Eliminando elementos del diccionario
del paises["COL"]
print(paises)

pais_obtenido = paises.pop("MEX")
print(f"El pais obtenido es: {pais_obtenido}")
print(paises)



"""
