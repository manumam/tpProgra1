from usuarios import users
from stock import stockConsumibles
import funcionesCanchas
import funcionesUsuarios

# # # # # PROGRAMA PRINCIPAL

anio = funcionesCanchas.iniciarCalendarioAnual()

totalRecaudado = 0
    
def desplegarMenu():
    flag = 0
    if(funcionesUsuarios.verificarUsuario()):
        print('----------------------------------------------------------------------- \n'
              'Bienvenido al sistema! \n'  
              'Qué desea hacer? \n'
              '1. Usuarios (No disponible aún). \n'
              '2. Canchas \n'
              '3. Estadísticas y reportes (No disponible aún). \n'
              '-----------------------------------------------------------------------')
        eleccionUsuario = input(int('Ingrese el numero correspondiente a la opción deseada: '))
        if(eleccionUsuario == 2):
            desplegarMenuCanchas()
            flag = 1
    else:
        print('ERROR. Usuario o contraseña incorrecto/a.')
        flag = 0
    return flag

def desplegarMenuCanchas():
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
    eleccionUsuario = input(int('Ingrese el numero correspondiente a la opción deseada: '))
    if(eleccionUsuario == 1):
        funcionesCanchas.consultarDisponibilidadMenu()
    elif(eleccionUsuario == 2):
        funcionesCanchas.tomarReservaMenu()
    elif(eleccionUsuario == 3):
        funcionesCanchas.cobrar()
    elif(eleccionUsuario == 4):
        funcionesCanchas.venderConsumibles()
    flag = 1
    return flag

print(anio)