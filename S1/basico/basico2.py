
# DÍA 2: Estructuras de Datos y Funciones

# 1. Listas
frutas = ["manzana", "banana", "naranja"]
frutas.append("pera")
frutas.insert(1, "uva")
print(frutas)
print(f"Los primeros dos elementos: {frutas[:2]}")

# Diccionarios
estudiante = {
    "nombre": "Juan",
    "edad": 20,
    "cursos": ["Python", "JavaScript", "SQL"]
}
print(f"Edad del estudiante: {estudiante['edad']}")
print(f"Primer curso: {estudiante['cursos'][0]}")

# 2. Funciones
def calcular_promedio(*numeros): # Parámetros variables
    return sum(numeros) / len(numeros)

print(f"Promedio: {calcular_promedio(10, 20, 30, 40)}")

# Función lambda
cuadrado = lambda x: x ** 2
print(f"Cuadrado de 5: {cuadrado(5)}")

# 3. List Comprehension
numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros if x % 2 == 0]
print(f"Cuadrados de números pares: {cuadrados}")