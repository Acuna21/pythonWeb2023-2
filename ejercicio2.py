#Capitulo 1 Reto
"""Un palíndromo es un una palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda ejemplo Ojo, Oso, Ana, Anna, Otto…

Su misión es, realizar un algoritmo que me permita conocer dada una palabra por el usuario si es palíndromo o no
"""

def palindromo(palabra:str):
    # Convertir la palabra a minúsculas 
    palabra = palabra.lower() 
    
    palabra = palabra.replace(" ", "")  # Eliminar espacios en blanco si los hay
    
    longitud = len(palabra)
    invertida = ""

    #Construir la palabra invertida caracter por caracter
    for i in range(longitud - 1, -1, -1):
        invertida += palabra[i]

    if palabra == invertida:
        return True
    else:
        return False

# Solicitar una palabra al usuario
palabra_usuario:str = input("Por favor, ingrese una palabra: ")

if palindromo(palabra_usuario):
    print(f"{palabra_usuario}-> Es un palíndromo.")
else:
    print(f"{palabra_usuario} ->No es un palíndromo.")
