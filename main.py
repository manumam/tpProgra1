import funcionesCanchas
import funcionesUsuarios

# # # # # PROGRAMA PRINCIPAL
    
def desplegarMenu(id):

    '''Esta funcion despliega el menu principal del programa. No tiene parametros de entrada y su salida es redirigir al usuario a la seccion del programa deseada.'''

    print('----------------------------------------------------------------------- \n'
            'Bienvenido al sistema! \n'  
            'Qué desea hacer? \n'
            '1. Usuarios. \n'
            '2. Canchas \n'
            '3. Estadísticas y reportes (No disponible aún). \n'
            '-----------------------------------------------------------------------')
    eleccionUsuario = int(input('Ingrese el numero correspondiente a la opción deseada: '))
    if(eleccionUsuario == 2):
        desplegarMenuCanchas()
    elif(eleccionUsuario == 1):
        desplegarMenuUsuarios(id)
    return

def desplegarMenuCanchas():

    '''Esta funcion despliega el menu de operaciones de las canchas del programa. No tiene parametros de entrada y su salida es ejecutar la funcion que desea el usuario.'''
    
    eleccionUsuario = 0
    flag = 0
    print('----------------------------------------------------------------------- \n'
              'CANCHAS \n'  
              'Qué desea hacer? \n'
              '1. Consultar Disponibilidad. \n'
              '2. Tomar reserva. \n'
              '3. Cobrar una cancha. \n'
              '4. Vender consumibles. \n'
              '-----------------------------------------------------------------------')
    eleccionUsuario = int(input('Ingrese el numero correspondiente a la opción deseada: '))
    if(eleccionUsuario == 1):
        funcionesCanchas.consultarDisponibilidadMenu()
        desplegarMenu()
    elif(eleccionUsuario == 2):
        funcionesCanchas.tomarReservaMenu()
        desplegarMenu()
    elif(eleccionUsuario == 3):
        funcionesCanchas.cobrar()
        desplegarMenu()
    elif(eleccionUsuario == 4):
        funcionesCanchas.venderConsumibles()
        desplegarMenu()
    flag = 1
    return flag

def desplegarMenuUsuarios(id):
    eleccionUsuario = 0
    flag = 0
    print('----------------------------------------------------------------------- \n'
              'USUARIOS \n'  
              'Qué desea hacer? \n'
              '1. Crear un producto. \n'
              '2. Modificar un precio. \n'
              '3. Cargar stock. \n'
              '4. Crear un usuario. (EXCLUSIVO PARA ADMIN) \n'
              '5. Administrar contraseña. (EXCLUSIVO PARA ADMIN)\n'
              '6. Modificar jerarquía de un usuario. (EXCLUSIVO PARA ADMIN)\n'
              '-----------------------------------------------------------------------')
    eleccionUsuario = int(input('Ingrese el numero correspondiente a la opción deseada: '))
    if(funcionesUsuarios.status(id) == "EMPLOYEE" and eleccionUsuario in [4,5,6]):
        print("Este usuario no tiene permisos suficiente para realizar esta acción. ")
        desplegarMenu(id)
    else:
        if(eleccionUsuario == 1):
            funcionesUsuarios.crearProducto()
        elif(eleccionUsuario == 2):
            funcionesUsuarios.mostrarProductos()
            id = int(input("Ingrese el id del producto que desea modificar. "))
            funcionesUsuarios.modificarPrecio(id)
        elif(eleccionUsuario == 3):
            funcionesUsuarios.mostrarProductos()
            id = int(input("Ingrese el id del producto que desea modificar. "))
            funcionesUsuarios.modificarStock(id)
        elif(eleccionUsuario == 4):
            funcionesUsuarios.crearUsuario()
        elif(eleccionUsuario == 5):
            funcionesUsuarios.mostrarUsuarios()
            id = int(input("Ingrese el id del usuario que desea modificar. "))
            funcionesUsuarios.administrarPassword(id)
        elif(eleccionUsuario == 6):
            funcionesUsuarios.mostrarUsuarios()
            id = int(input("Ingrese el id del usuario que desea modificar. "))
            funcionesUsuarios.cambiarStatus(id)
        


def main():
    funcionesUsuarios.mostrarUsuarios()
    user = int(input('Ingrese su id de usuario. '))
    if(funcionesUsuarios.verificarUsuario(user)):
        desplegarMenu(user)
    return user

main()