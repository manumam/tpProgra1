from main import anio
from stock import stockConsumibles

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

def diaDeLaSemana(dia):
    
    '''Define que dia de la semana cae el dia que consultamos. Recibe como entrada un entero y tiene como salida un entero.'''

    diaDeLaSemana = dia % 7
    return diaDeLaSemana

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
    semana = definirSemana(definirCantDiasTotales(dia, mes))
    queDiaCae = diaDeLaSemana(definirCantDiasTotales(dia, mes))
    disponibilidad, valor = disponibilidadTurno(dia, mes, turno, anio)
    flag = -1
    if (disponibilidad != 0):
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
        flag = 1
    else:
        flag = -1
    
    return flag
    
def insertarTurno(dia, mes, turno, anio):
    if(insertarTurnoAux(dia, mes, turno, anio) == 1):
        print('Turno agendado.')
    elif(insertarTurnoAux(dia, mes, turno, anio) == -1):
        print('Horario NO disponible.')

def consultarDisponibilidadMenu():
    flag = 0
    mes = input(int('Qué mes desea consultar? '))
    dia = input(int('Qué dia desea consultar? '))
    turno = input(int('En que horario desea? '))
    if(disponibilidadTurno(dia, mes, turno, anio) == 0):
        print('No hay cancha disponible para el dia y turno seleccionado.')
    elif(disponibilidadTurno(dia, mes, turno, anio) in [1,2,3]):
        print('Hay cancha disponible para el dia y turno seleccionado. Desea reservar el turno? ')
        reservar = input(int('Ingrese 1 si desea hacer la reserva sobre este dia y horario o 2 si no lo desea.'))
        if(reservar == 1):
            insertarTurno(dia,mes,turno,anio)
    flag = 1
    return flag

def tomarReservaMenu():
    flag = 0
    mes = input(int('Qué mes desea consultar? '))
    dia = input(int('Qué dia desea consultar? '))
    turno = input(int('En que horario desea? '))
    if(disponibilidadTurno(dia, mes, turno, anio) in [1,2,3]):
        insertarTurno(dia,mes,turno,anio)
    elif(disponibilidadTurno(dia, mes, turno, anio) == 0):
        print('No hay cancha disponible para el dia y turno seleccionado.')
    flag = 1
    return flag

def cobrar():
        dia = input(int('Ingrese el dia de hoy. '))
        mes = input(int('Ingrese el mes actual. '))
        turno = input(int('Ingrese el turno actual. '))
        cancha = input(int('Ingrese la cancha que desea cobrar. '))
        aCobrar = 0
        if(cancha == 1):
            if(disponibilidadTurno(dia, mes, turno, anio) in [0, 2, 3]):
                aCobrar = precioCancha + consumiblesCancha1
                totalRecaudado += aCobrar
                print(f'El importe a cobrar es de {aCobrar}.')
            else:
                print('ERROR. Turno ingresado disponible.')
        elif(cancha == 2):
            if(disponibilidadTurno(dia, mes, turno, anio) in [0, 3]):
                aCobrar = precioCancha + consumiblesCancha2
                totalRecaudado += aCobrar
                print(f'El importe a cobrar es de {aCobrar}.')
            else:
                print('ERROR. Turno ingresado disponible.')
        elif(cancha == 3):
            if(disponibilidadTurno(dia, mes, turno, anio) == 0):
                aCobrar = precioCancha + consumiblesCancha3
                totalRecaudado += aCobrar
                print(f'El importe a cobrar es de {aCobrar}.')
            else:
                print('ERROR. Turno ingresado disponible.')
        
imprimirPrecioCancha = lambda : print(f'El precio de la cancha por 1 hora es de: {precioCancha}')

imprimirRecaudacion = lambda : print(f'El total recaudado es de {totalRecaudado}')

def venderConsumibles():
    cancha = input(int('A que cancha desea cargar esta compra? '))
    producto = 0
    print('Los articulos disponibles son: ')
    while(producto != -1):
        for _ in range(len(stockConsumibles)):
            if(stockConsumibles[_]['stockRestante'] > 0):
                print(f'{stockConsumibles[_]['id']}. {stockConsumibles[_]['producto']} \n')
        producto = input(int('Ingrese el numero del producto que desea agregar a la cuenta. Ingrese -1 para finalizar.'))
        if(cancha == 1):
            consumiblesCancha1 += stockConsumibles[producto - 1]['precio'] 
        elif(cancha == 2):
            consumiblesCancha2 += stockConsumibles[producto - 1]['precio'] 
        elif(cancha == 3):
            consumiblesCancha3 += stockConsumibles[producto - 1]['precio']


    

    