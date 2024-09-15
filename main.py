from usuarios import users
from stock import stockConsumibles
import funcionesCanchas
import funcionesUsuarios

# # # # # PROGRAMA PRINCIPAL
    
def desplegarMenu():

    '''Esta funcion despliega el menu principal del programa. No tiene parametros de entrada y su salida es redirigir al usuario a la seccion del programa deseada.'''

    flag = 0
    print('----------------------------------------------------------------------- \n'
            'Bienvenido al sistema! \n'  
            'Qué desea hacer? \n'
            '1. Usuarios (No disponible aún). \n'
            '2. Canchas \n'
            '3. Estadísticas y reportes (No disponible aún). \n'
            '-----------------------------------------------------------------------')
    eleccionUsuario = int(input('Ingrese el numero correspondiente a la opción deseada: '))
    if(eleccionUsuario == 2):
        desplegarMenuCanchas()
        flag = 1
    return flag

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

def main():
    if(funcionesUsuarios.verificarUsuario()):
        desplegarMenu()

main()