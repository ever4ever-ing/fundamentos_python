# DÍA 3: Programación Avanzada

# 1. Manejo de Errores
def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Error: División por cero"
    except TypeError:
        return "Error: Tipo de datos incorrecto"

print(dividir(10, 2))
print(dividir(10, 0))

# 2. Trabajo con Archivos
# Escribir en un archivo
with open("ejemplo.txt", "w") as archivo:
    archivo.write("Hola, este es un archivo de ejemplo.\n")
    archivo.write("Segunda línea del archivo.")

# Leer el archivo
with open("ejemplo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

# 3. Mini Proyecto: Calculadora Simple
def calculadora():
    while True:
        print("\nCalculadora Simple")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        opcion = input("Elige una opción (1-5): ")
        
        if opcion == '5':
            print("¡Hasta luego!")
            break
            
        if opcion not in ['1', '2', '3', '4']:
            print("Opción no válida")
            continue
            
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        if opcion == '1':
            print(f"Resultado: {num1 + num2}")
        elif opcion == '2':
            print(f"Resultado: {num1 - num2}")
        elif opcion == '3':
            print(f"Resultado: {num1 * num2}")
        elif opcion == '4':
            try:
                print(f"Resultado: {num1 / num2}")
            except ZeroDivisionError:
                print("Error: No se puede dividir por cero")

# Para ejecutar la calculadora, descomenta la siguiente línea:
# calculadora()