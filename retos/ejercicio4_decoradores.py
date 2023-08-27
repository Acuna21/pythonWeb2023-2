"""Diseña un sistema de autenticación multinivel utilizando decoradores en Python. Debes implementar tres niveles de autenticación: usuario, administrador y superusuario. Cada nivel debe requerir credenciales específicas para acceder a ciertas funciones. Utiliza decoradores para verificar la autorización antes de permitir el acceso a las funciones correspondientes.
"""
# Definición de decoradores
def requerir_autenticacion(niveles):
    
    # Este es el decorador para verificar la autorización
    def decorador(funcion):
        # Esta es la que se ejecutará 
        def prueba(usuario, *args, **kwargs):
            # Verifica si el usuario tiene un token de sesión y pertenece al nivel requerido
            if usuario['sesion']['token'] and usuario['rol'] in niveles:
                # Si es así, se ejecuta la función original con los argumentos dados
                funcion(usuario, *args, **kwargs)
            else:
                # Si no cumple los requisitos de autenticación, muestra un mensaje de acceso denegado
                print("Acceso denegado. Debes gestionar los permisos suficientes")
        return prueba
    return decorador

# Definición de niveles de autenticación utilizando el decorador requerir_autenticacion
nivel_usuario = requerir_autenticacion(['free', 'admin', 'supadmin'])
nivel_admin = requerir_autenticacion(['admin', 'supadmin'])
nivel_superusuario = requerir_autenticacion(['supadmin'])

# Definición de funciones para autenticación, decoradas con los niveles requeridos
@nivel_usuario
def inicio(usuario):
    print("Bienvenido al área de usuarios")

@nivel_admin
def eliminar_usuario(usuario):
    print("Usuario Eliminado")

@nivel_admin
def crear_usuario(usuario):
    print("Usuario creado")

@nivel_superusuario
def gestionar_sistema(usuario):
    print("Gestionando el sistema como Supervisor de Usuarios")

# Ejemplo de usuario con sus detalles
usuario = {
    'correo': "acunabe@gmail.com",
    'rol': 'free', 
    'sesion': {
        'token': True
    } 
}

# Ejemplos de llamadas a las funciones decoradas con los niveles de autenticación
inicio(usuario)            # El usuario tiene el nivel 'free' que permite acceder a esta función
eliminar_usuario(usuario)  # El usuario tiene el nivel 'free', pero esta función requiere 'admin' o 'supadmin'
crear_usuario(usuario)     # Mismo caso que eliminar_usuario
gestionar_sistema(usuario) # Mismo caso que eliminar_usuario

