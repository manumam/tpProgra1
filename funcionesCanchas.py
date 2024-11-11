import json
from funcionesUsuarios import obtenerPosicionPorProducto

precioCancha = 18000

consumiblesCancha1 = 0

consumiblesCancha2 = 0

consumiblesCancha3 = 0

totalRecaudado = 0

def iniciarCalendarioSemanal():

    '''Inicia una matriz de 17 filas y 8 columnas con todos los campos con el valor '000'. No tiene entradas y tiene como salida la matriz generada.'''

    filas = 17
    columnas = 8
    semana = []
    for _ in range(filas):
        semana.append(['000'] * columnas)
    return semana
    
def iniciarCalendarioAnual():
    
    '''Inicia una lista de 52 posiciones de matrices generadas con la funcion iniciarCalendarioSemanal. No tiene entradas y tiene como salida la lista de matrices generada.'''

    anio = []
    for _ in range(52):
        semana = iniciarCalendarioSemanal()
        anio.append(semana)
    return anio

anio = iniciarCalendarioAnual()

def definirCantDiasTotales(dia, mes):
    
    '''Define cuantos dias pasaron en el año para un determinado dia de un determinado mes. Recibe como entradas el dia y el mes y tiene como salida el numero de dias que pasaron hasta esa fecha en el año.'''

    diasPorMes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    diasTotales = 0
    for i in range(mes):
        diasTotales += diasPorMes[i]
    
    diasTotales += dia
    return diasTotales

def definirSemana(dia):
    
    '''Define a que intervalo de 7 dias pertenece un dia del año. Recibe como entrada un entero y devuelve como salida otro entero.'''

    semana = 1
    semana = semana + (dia // 7)
    return semana 

diaDeLaSemana = lambda dia : dia % 7

def disponibilidadTurno(dia, mes, turno, anio):
    
    '''Nos dice si hay alguna cancha disponible o no. En caso de que haya una disponible, nos dice cual. Recibe como entrada el dia, mes y turno deseado para la reserva y la lista de matrices del año. Tiene como salida un string que nos dice la disponibilidad de las canchas.'''

    semana = definirSemana(definirCantDiasTotales(dia, mes))
    queDiaCae = diaDeLaSemana(definirCantDiasTotales(dia, mes))
    disponible = ''
    valor = anio[semana][turno][queDiaCae]
    if(anio[semana][turno][queDiaCae] == '111'):
        disponible = 0
    else:
        if(anio[semana][turno][queDiaCae] == '000' or anio[semana][turno][queDiaCae] == '010' or anio[semana][turno][queDiaCae] == '001' or anio[semana][turno][queDiaCae] == '011'):
            disponible = 1
        elif(anio[semana][turno][queDiaCae] == '100' or anio[semana][turno][queDiaCae] == '101'):
            disponible = 2
        elif(anio[semana][turno][queDiaCae] == '110'):
            disponible = 3
    return disponible, valor

def insertarTurnoAux(dia, mes, turno, anio):

    '''Esta funcion inserta un turno nuevo en el sistema modificando la matriz central. Recibe el dia, mes y turno junto con la matriz central y no tiene valor de salida.'''

    semana = definirSemana(definirCantDiasTotales(dia, mes))
    queDiaCae = diaDeLaSemana(definirCantDiasTotales(dia, mes))
    disponibilidad, valor = disponibilidadTurno(dia, mes, turno, anio)
    flag = -1
    if (disponibilidad != 0):
        flag = 1
        if(disponibilidad == 1):
            if(valor == '000'):
                anio[semana][turno][queDiaCae] = '100'
            elif(valor == '010'):
                anio[semana][turno][queDiaCae] = '110'
            elif(valor == '001'):
                anio[semana][turno][queDiaCae] = '101'
            elif(valor == '011'):
                anio[semana][turno][queDiaCae] = '111'
        if(disponibilidad == 2):
            if(valor == '100'):
                anio[semana][turno][queDiaCae] = '110'
            elif(valor == '101'):
                anio[semana][turno][queDiaCae] = '111'
        if(disponibilidad == 3):
            anio[semana][turno][queDiaCae] = '111'
    else:
        flag = -1
    
    return flag
    
def insertarTurno(dia, mes, turno, anio):

    '''Esta funcion llama a la funcion insertarTurnoAux e imprime un mensaje dependiendo del resultado de este llamado. Recibe como parametros el dia, mes y turno junto con la matriz central y tiene como salida los mensajes mencionados anteriormente.'''


    status = insertarTurnoAux(dia, mes, turno, anio)
    if(status == 1):
        print('Turno agendado.')
    elif(status == -1):
        print('Horario NO disponible.')

def consultarDisponibilidadMenu():

    '''Esta funcion pide al usuario los datos de un turno y luego llama a la funcion disponibilidad turno con esos datos. A partir del resultado de ese llamado imprime un mensaje. No recibe parametros y tiene mensajes por consola como salida.'''

    flag = 0
    mes = int(input('Qué mes desea consultar? '))
    dia = int(input('Qué dia desea consultar? '))
    turno = int(input('En que horario desea? '))
    disponibilidad, valor = disponibilidadTurno(dia, mes, turno, anio)
    if(disponibilidad == 0):
        print('No hay cancha disponible para el dia y turno seleccionado.')
    elif(disponibilidad in [1,2,3]):
        print('Hay cancha disponible para el dia y turno seleccionado. Desea reservar el turno? ')
        reservar = int(input('Ingrese 1 si desea hacer la reserva sobre este dia y horario o 2 si no lo desea.'))
        if(reservar == 1):
            insertarTurno(dia,mes,turno,anio)
    flag = 1
    return flag

def tomarReservaMenu():

    '''Esta funcion pide al usuario los datos de un turno y luego llama a la funcion disponibilidad turno con esos datos. A partir del resultado de ese llamado inserta un turno o imprime un mensaje. No recibe parametros y tiene mensajes por consola como salida.'''

    flag = 0
    mes = int(input('Qué mes desea consultar? '))
    dia = int(input('Qué dia desea consultar? '))
    turno = int(input('En que horario desea? '))
    disponibilidad, valor = disponibilidadTurno(dia, mes, turno, anio)
    if(disponibilidad in [1,2,3]):
        insertarTurno(dia,mes,turno,anio)
    elif(disponibilidad == 0):
        print('No hay cancha disponible para el dia y turno seleccionado.')
    flag = 1
    return flag

def cobrar():

    '''Esta funcion cobra la cuenta de una cancha para un dia, mes y horario particular del año. Suma esa cifra a lo recaudado total y obtiene la cuenta de las variables globales definidas al principio de este documento. No recibe parametros de entrada y tiene como salida un mensaje incluyendo el total a cobrar.'''

    dia = int(input('Ingrese el dia de hoy. '))
    mes = int(input('Ingrese el mes actual. '))
    turno = int(input('Ingrese el turno actual. '))
    cancha = int(input('Ingrese la cancha que desea cobrar. '))
    aCobrar = 0
    global totalRecaudado
    disponibilidad, valor = disponibilidadTurno(dia, mes, turno, anio)
    if(cancha == 1):
        if(disponibilidad in [0, 2, 3]):
            aCobrar = precioCancha + consumiblesCancha1
            totalRecaudado += aCobrar
            print(f'El importe a cobrar es de {aCobrar}.')
        else:
            print('ERROR. Turno ingresado disponible.')
    elif(cancha == 2):
        if(disponibilidad in [0, 3]):
            aCobrar = precioCancha + consumiblesCancha2
            totalRecaudado = totalRecaudado + aCobrar
            print(f'El importe a cobrar es de {aCobrar}.')
        else:
            print('ERROR. Turno ingresado disponible.')
    elif(cancha == 3):
        if(disponibilidad == 0):
            aCobrar = precioCancha + consumiblesCancha3
            totalRecaudado = totalRecaudado + aCobrar
            print(f'El importe a cobrar es de {aCobrar}.')
        else:
            print('ERROR. Turno ingresado disponible.')

def deducirStock(id):
    try:
        with open("stock.json", "rt") as stock:
            productos = json.load(stock)
    except IOError:
        print("Error al acceder al archivo. ")

    for item in productos:
        if (item["id"] == id):
            producto = item["producto"]
            precio = item["precio"]
            cantidad = item["cantidad"] - 1
    
    registro = {"id": id, "producto": producto, "precio": precio, "cantidad": cantidad}
    posicion = obtenerPosicionPorProducto(id)
    productos.pop(posicion)
    productos.append(registro)

    try:
        with open("stock.json", "wt") as stock:
            json.dump(productos, stock, indent=4)
    except IOError:
        print("Error al intentar acceder al archivo.")


def venderConsumibles():

    '''Esta funcion muestra una lista de todos los productos consumibles disponibles para comprar y pide al usuario ingresar qué articulos desea agregar a la cuenta. A medida que se ingresan los va sumando a la cuenta de la cancha. No tiene parametros de entrada salida, solo modifica el valor de la cuenta.'''

    cancha = int(input('A que cancha desea cargar esta compra? '))
    producto = 1
    global consumiblesCancha1
    global consumiblesCancha2
    global consumiblesCancha3
    print('Los articulos disponibles son: ')
    
    try:
        with open("stock.json", "rt") as stock:
            productos = json.load(stock)
    except IOError:
        print("Error al acceder al archivo. ")

    for producto in productos:
        print(f"{producto["id"]}. {producto["producto"]} ${producto["precio"]}")

    seleccionado = int(input('Ingrese el id del producto que desea agregar a la cuenta. Ingrese -1 para finalizar. '))
    
    for producto in productos:
        if(producto["id"] == seleccionado):
            precio = producto["precio"]

    deducirStock(seleccionado)

    if(cancha == 1):
        consumiblesCancha1 = precio
        print(consumiblesCancha1)
    elif(cancha == 2):
        consumiblesCancha2 = precio
        print(consumiblesCancha2)
    elif(cancha == 3):
        consumiblesCancha3 = precio
        print(consumiblesCancha3)