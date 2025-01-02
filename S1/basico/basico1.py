# Fundamentos Básicos

# 1. Variables y Tipos de Datos
nombre = "María"
edad = 25
altura = 1.65
es_estudiante = True

print(f"Tipo de nombre: {type(nombre)}")
print(f"Tipo de edad: {type(edad)}")
print(f"Tipo de altura: {type(altura)}")
print(f"Tipo de es_estudiante: {type(es_estudiante)}")

# Conversión de tipos
numero_texto = "100"
numero = int(numero_texto)
print(f"Texto convertido a número: {numero + 50}")

# 2. Operadores
# Aritméticos

a = 10
b = 3
print(f"Suma: {a + b}")
print(f"Resta: {a - b}")
print(f"Multiplicación: {a * b}")
print(f"División: {a / b}")
print(f"División entera: {a // b}")
print(f"Módulo: {a % b}")
print(f"Potencia: {a ** b}")

# 3. Estructuras de Control
# If-elif-else

# Ejercicio: Preguntar la edad y mostrar si es menor de edad,
# mayor de edad o acaba de cumplir la mayoría de edad
edad = 18
if edad < 18:
    print("Eres menor de edad")
elif edad == 18:
    print("Acabas de cumplir la mayoría de edad")
else:
    print("Eres mayor de edad")

# For loop
for i in range(5):
    print(f"Iteración {i}")

# While loop con break
contador = 0
while True:
    print(contador)
    contador += 1
    if contador >= 5:
        break