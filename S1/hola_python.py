print("¡Hola desde Python!")

lenguaje = "Hola de nuevo Python" # Variable que almacena un string de texto

print(lenguaje)

numero = 20 # Variable que almacena un número entero

print(numero) #Imprimir por consola el numero almacenado en la variable

lista_vacia = []

gatos = ["Garfield", "Silvestre", "Hello Kitty"]

print(gatos[2])

gatos[1] = "Tom"

print(gatos)

gatos.append("Felix")

print(gatos)

gatos.pop()

print(gatos)

perro = ("Scooby Doo", "Gran Danés", "Scooby Galletas", 7)

print(perro[0]) #Imprime: Scooby Doo

#perro[2] = "comida de perro" #Error: No se puede modificar una tupla

persona = {'nombre': 'Carmen',
            'edad': 31,
            'altura': 1.71,
            'usa_lentes': False}

persona['nombre'] = 'Valeria'
persona['edad'] = 25 

print(persona)

persona['hobbies'] = ['jugar videojuegos', 'programación'] 
print(persona)

altura = persona.pop('altura') 
print("Quitando llave con pop:")
print(persona)
print(altura) #Imprime: 1.71