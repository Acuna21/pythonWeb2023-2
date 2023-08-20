#Capitulo 2 Reto
"""Dado dos diccionarios 1 de productos y el 2 de categoría, conocer un 3 que permita tener el nombre del producto y el nombre de su categoría ejemplo.
"""

#Diccionarios 
libros = {
    "Cien años de soledad": {
        "autor": "Gabriel García Márquez",
        "categoria": "Ficción"
    },
    "El principito": {
        "autor": "Antoine de Saint-Exupéry",
        "categoria": "Literatura infantil"
    },
    "Sin salida": {
        "autor": "George Orwell",
        "categoria": "Ciencia ficción"
    },
    "Orgullo y prejuicio": {
        "autor": "Jane Austen",
        "categoria": "Romance"
    }
}

# Diccionario de categorías con descripciones
categorias = {
    "Ficción": "Obras de narrativa imaginativa",
    "Literatura infantil": "Libros aptos para niños y jóvenes",
    "Ciencia ficción": "Narrativas especulativas basadas en ciencia y tecnología",
    "Romance": "Historias de amor y relaciones personales"
}

# Crear un diccionario que relaciona libros con sus categorías y autores
libros_con_categorias = {}

for libro, detalles in libros.items():
    categoria_descripcion = categorias.get(detalles["categoria"], "Categoría desconocida")
    autor = detalles["autor"]
    libros_con_categorias[libro] = {"autor": autor, "categoria": categoria_descripcion}

# Imprimir el diccionario de libros con sus detalles
for libro, detalles in libros_con_categorias.items():
    autor = detalles["autor"]
    categoria = detalles["categoria"]
    print(f"Libro: {libro}, Autor: {autor}, Categoría: {categoria}")
