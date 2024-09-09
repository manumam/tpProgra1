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
        disponible = 'No hay cancha'
    else:
        cancha1Vacia = ['000', '010', '001', '011']
        cancha2Vacia = ['100', '101']
        cancha3Vacia = ['110']
        if(anio[semana][turno][queDiaCae] in cancha1Vacia):
            disponible = 'Cancha 1'
        elif(anio[semana][turno][queDiaCae] in cancha2Vacia):
            disponible = 'Cancha 2'
        elif(anio[semana][turno][queDiaCae] in cancha3Vacia):
            disponible = 'Cancha 3'
    return disponible, valor

def insertarTurnoAux(dia, mes, turno, anio):

    """Modifica el valor en la tabla para reservar un turno nuevo si está disponible, si no está disponible no hace nada.
    Toma como entradas el dia, mes y turno y la lista de matrices y devuelve si el turno fue reservado o no."""

    semana = definirSemana(definirCantDiasTotales(dia, mes))
    queDiaCae = diaDeLaSemana(definirCantDiasTotales(dia, mes))
    disponibilidad, valor = disponibilidadTurno(dia, mes, turno, anio)
    flag = -1
    if (disponibilidad != 'No hay cancha'):
        if(disponibilidad == 'Cancha 1'):
            if(valor == '000'):
                anio[semana][turno][queDiaCae] = '100'
            elif(valor == '010'):
                anio[semana][turno][queDiaCae] = '110'
            elif(valor == '001'):
                anio[semana][turno][queDiaCae] = '101'
            elif(valor == '011'):
                anio[semana][turno][queDiaCae] = '111'
        if(disponibilidad == 'Cancha 2'):
            if(valor == '100'):
                anio[semana][turno][queDiaCae] = '110'
            elif(valor == '101'):
                anio[semana][turno][queDiaCae] = '111'
        if(disponibilidad == 'Cancha 3'):
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