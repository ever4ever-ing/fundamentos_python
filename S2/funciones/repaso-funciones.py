"""
Multiplica por 2: crea una función que reciba un número y 
devuelva una lista que contenga los números enteros multiplicados por dos, 
desde el 0 hasta el número proporcionado como entrada.
Ejemplo: multiplica_por_2(5) debe regresar [0, 2, 4, 6, 8, 10]
"""

def multiplica_por_2(n):
    lista = []
    for i in range(0, n+1, 1):
        print(i)
        lista.append(i*2) # agregar elemento a la lista
    return lista

lista_obtenida = multiplica_por_2(8) # llamamos a la funcion
print(lista_obtenida)


"""
Suma y resta: crea una función que reciba una lista con dos números. 
Imprime la suma de los dos números y regresa la resta de los dos números.
Ejemplo: suma_y_resta([5, 4]) debe de imprimir 9 y regresar 1
"""

def suma_y_resta(lista):
    a = lista[0]
    b = lista[1]
    print(a+b)


suma_y_resta()
