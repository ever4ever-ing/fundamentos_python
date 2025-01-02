import requests

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def crear_desde_diccionario(cls, datos):
        try:
            nombre = datos['nombre']
            edad = datos['edad']
            return cls(nombre, edad)
        except KeyError as e:
            print(f"Error: Falta el campo {e} en los datos.")
            return None

    def mostrar_info(self):
        print(f'Nombre: {self.nombre}, Edad: {self.edad}')

# Uso del método de clase
datos = {'nombre': 'Juan', 'edad': 30}
persona = Persona.crear_desde_diccionario(datos)
if persona:
    persona.mostrar_info()

# Uso de la clase requests para simular una consulta a una API
"""
Este ejemplo muestra cómo se puede utilizar el método de clase 
crear_desde_diccionario para crear una instancia de Persona a
partir de datos recibidos de una API en formato JSON.
"""
try:
    # Simulación de una consulta a una API
    response = requests.get('http://127.0.0.1:5000/persona/1')
    response.raise_for_status()  # Verifica si la solicitud fue exitosa
    datos = response.json()  # Suponiendo que la respuesta es un JSON con 'nombre' y 'edad'
    persona = Persona.crear_desde_diccionario(datos)
    if persona:
        persona.mostrar_info()
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud a la API: {e}")
except ValueError:
    print("Error: La respuesta de la API no es un JSON válido.")