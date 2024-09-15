from usuarios import users

usuarioEnSesion = ''

def verificarUsuario():

    """Verifica si el usuario y la contraseña y existen y son correctos entre si. No recibe parametros y tiene como salida un valor booleano."""

    nombresUsuarios = []
    for i in range(len(users)):
        nombresUsuarios.append(users[i]['id'])
    
    user = str(input('Bienvenido al sistema. Ingrese su nombre de usuario. '))
    verificacion = False
    if(user in nombresUsuarios):
        pwd = str(input('Ingrese su contraseña. '))
        for i in range(len(users)):
            if(users[i]['id'] == user):
                verificacion = users[i]['password'] == pwd
                if(verificacion):
                    usuarioEnSesion = users[i]['id']
                return verificacion
    else:
        return verificacion
