numero1 = 70
numero2 = 3.14
booleano = False
cadena = 'Hola Mundo'
ingredientes_pastel = ['Harina', 'Leche', 'Huevos', 'Vainilla', 'Chocolate']
persona = {'nombre': 'Patricio', 'pais': 'México', 'edad': 35, 'soltero': False}
frutas = ('guayaba', 'fresa', 'papaya')
print(type(frutas))
print(ingredientes_pastel[2])
ingredientes_pastel.append('Mantequilla')
print(persona['nombre'])
persona['nombre'] = 'Kevin'
persona['color_ojos'] = 'cafe'
print(frutas[2])

if numero1 > 45:
    print("Numero mayor")
else:
    print("Numero menor")

if len(cadena) < 5:
    print("Cadena corta")
elif len(cadena) > 15:
    print("Cadena larga")
else:
    print("Cadena perfecta")

for x in range(8):
    print(x)
for x in range(2,8):
    print(x)
for x in range(2,8,2):
    print(x)

x = 0
while(x < 8):
    print(x)
    x += 1

ingredientes_pastel.pop() # Elimina el último elemento
ingredientes_pastel.pop(1) # Elimina el elemento en la posición 1

print(persona)
persona.pop('color_ojos')
print(persona)
ingredientes_pastel.append('Mantequilla')
for ingrediente in ingredientes_pastel:
    if ingrediente == 'Harina' or ingrediente == 'Mantequilla':
        print(ingrediente)
        continue # Salta a la siguiente iteración
    print('Después de la primera sentencia')
    if ingrediente == 'Chocolate':
        print("Encontré el chocolate")
        break # Sale del ciclo
        

def imprime_hola_10_veces(): # Definición de la función
    for numero in range(10):
        print('Hola')
    print('10 veces hola terminado.-------------------')

imprime_hola_10_veces() # Llamada a la función

def imprime_hola_n_veces(n):
    for numero in range(n):
        print('Hola')
    print(f'{n} veces hola terminado.-------------------')

imprime_hola_n_veces(5)

def imprime_hola_n_o_diez_veces(n = 7):
    for numero in range(n):
        print('Hola')
    print(f'{n} veces hola terminado.-------------------')

imprime_hola_n_o_diez_veces() # toma el valor por defecto
imprime_hola_n_o_diez_veces(5) # toma el valor que se le pasa


print(len(persona))

"""
Sección BONUS
"""

# print(numero3)
# numero3 = 86
# frutas[0] = 'naranja'
# print(persona['hobbies'])
# print(ingredientes_pastel[11])
#   print(booleano)
# frutas.append('manzana')
# frutas.pop(1)