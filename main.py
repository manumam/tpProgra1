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
    queDiaCae = diaDeLaSemana(dia)
    disponible = ''
    if(anio[semana][turno][queDiaCae] == '111'):
        disponible = 'No hay cancha'
    else:
        if(anio[semana][turno][queDiaCae] == '000' or anio[semana][turno][queDiaCae] == '010' or anio[semana][turno][queDiaCae] == '001' or anio[semana][turno][queDiaCae] == '011'):
            disponible = 'Cancha 1'
        elif(anio[semana][turno][queDiaCae] == '100' or anio[semana][turno][queDiaCae] == '101'):
            disponible = 'Cancha 2'
        elif(anio[semana][turno][queDiaCae] == '110'):
            disponible = 'Cancha 3'
    return disponible