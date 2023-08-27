"""APRENDIENDO DECORADPRES en python"""

"""Diseña un sistema de autenticación multinivel utilizando decoradores en Python. Debes implementar tres niveles de autenticación: usuario, administrador y superusuario. Cada nivel debe requerir credenciales específicas para acceder a ciertas funciones. Utiliza decoradores para verificar la autorización antes de permitir el acceso a las funciones correspondientes.
"""
# Paso 1: Credenciales de los usuarios
usuarios = {
    "usuario": "usuario123",
    "administrador": "administrador123",
    "superusuario": "superusuario123"
}

# Paso 2: Definir los decoradores de autenticación
def autenticacion_usuario(func):
    def wrapper(username, password, *args, **kwargs):
        if usuarios.get(username) == password:
            return func(username, *args, **kwargs)
        else:
            return "Error de autenticación para el nivel de usuario"
    return wrapper

def autenticacion_administrador(func):
    def wrapper(username, password, *args, **kwargs):
        if username == "administrador" and usuarios.get(username) == password:
            return func(username, *args, **kwargs)
        else:
            return "Error de autenticación para el nivel de administrador"
    return wrapper

def autenticacion_superusuario(func):
    def wrapper(username, password, *args, **kwargs):
        if username == "superusuario" and usuarios.get(username) == password:
            return func(username, *args, **kwargs)
        else:
            return "Error de autenticación para el nivel de superusuario"
    return wrapper

# Paso 3: Definir funciones que requieran diferentes niveles de autenticación
@autenticacion_usuario
def funcion_usuario(username):
    return f"Bienvenido, {username}. --> Has accedido como USUARIO."

@autenticacion_administrador
def funcion_administrador(username):
    return f"Genial, {username}. --> Has accedido como ADMINISTRADOR."

@autenticacion_superusuario
def funcion_superusuario(username):
    return f"Hola, {username}.--> Has accedido como SUUPERUSUARIO."

# Paso 4: Prueba de las funciones
if __name__ == "__main__":
    usuario = "usuario"
    contrasena = "usuario123"
    print(funcion_usuario(usuario, contrasena))
    
    administrador = "administrador"
    contrasena_admin = "administrador123"
    print(funcion_administrador(administrador, contrasena_admin))
    
    superusuario = "superusuario"
    contrasena_super = "superusuario123"
    print(funcion_superusuario(superusuario, contrasena_super))
