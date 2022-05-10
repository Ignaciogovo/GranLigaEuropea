from cgi import print_arguments
import sys

from pandas import array
sys.path.append('ProyectoLiga\ProyectoLigaInventada\ProyectoNuevo\python\webscraping')
import conexionsql as cs
import random as ra


def ordenarJugadores(array,key):
    for i in range(0,len(array)):
        for a in range(i+1,len(array)):
            numero1 = array[i]
            numero2 = array[a]
            if (numero2[key]>numero1[key]):
                    intermedio = numero2
                    array[a] = array[i]
                    array[i] = intermedio
    return(array)
# Elección del sistema de un equipo
def sistemasEquipo():
    sistema = ra.randint(0,3)
    if sistema==0:
        sistema = [1,4,4,2]
    if sistema==1:
        sistema = [1,4,4,2]
    if sistema==2:
        sistema = [1,4,3,3]
    if sistema==3:
        sistema = [1,5,3,2]
    return(sistema)
# Calculo total de tarjetas de un equipo
def tarjetasTotales():
    amarillas = ra.randrange(0,5)
    rojas=(ra.randrange(0,3)*ra.randrange(0,4))/2
    if rojas < 1:
        rojas = 0
    tarjetas=[amarillas,rojas]
    return(tarjetas)

def asignarProbabilidades(jugadores):
    for i in range(0,len(jugadores)):
        ptitular = ra.randrange(0,11)
        pgol = ra.randrange(0,11)
        pamarilla = ra.randrange(0,11)
        proja = ra.randrange(0,11)
        pasis = ra.randrange(0,11)
        (jugadores[i])["ptitular"] = ptitular
        (jugadores[i])["titular"] = 0
        (jugadores[i])["pgol"] = pgol
        (jugadores[i])["gol"] = 0
        (jugadores[i])["pasis"] = pasis
        (jugadores[i])["asis"] = 0
        (jugadores[i])["pamarilla"] = pamarilla
        (jugadores[i])["amarilla"] = 0
        (jugadores[i])["proja"] = proja
        (jugadores[i])["roja"] = 0
    return(jugadores)


def mejorarPotencial(jugadores,opcion):
    #Multiplicadores
    if opcion == "ptitular":
        multiplicador = [15,30,30,30]
    if opcion == "pgol":
        multiplicador = [1,30,35,45]
    if opcion == "pasis":
        multiplicador = [1,30,45,35]
    if opcion == "pamarilla":
        multiplicador = [1,10,5,5]
    if opcion == "proja":
        multiplicador = [1,10,5,5]
    # AsignarMultiplicadores
    for i in range(0,len(jugadores)):
        jugador = jugadores[i]
        # Portero
        if jugador["posicion"] == "Portero":
            potenciador = multiplicador[0]/10
            if potenciador <=0:
                potenciador = 0.2
            jugador[opcion]=jugador[opcion]*potenciador
            jugadores[i]=jugador
            multiplicador[0]= multiplicador[0]-5
        # Defensa
        if jugador["posicion"] == "Defensa":
            potenciador = multiplicador[1]/10
            if potenciador <=0:
                potenciador = 0.2
            jugador[opcion]=jugador[opcion]*potenciador
            jugadores[i]=jugador
            multiplicador[1]= multiplicador[1]-5
        # Centrocampista
        if jugador["posicion"] == "Centrocampista":
            potenciador = multiplicador[2]/10
            if potenciador <=0:
                potenciador = 0.2
            jugador[opcion]=jugador[opcion]*potenciador
            jugadores[i]=jugador
            multiplicador[2]= multiplicador[2]-5
        # Delantero
        if jugador["posicion"] == "Delantero":
            potenciador = multiplicador[3]/10
            if potenciador <=0:
                potenciador = 0.2
            jugador[opcion]=jugador[opcion]*potenciador
            jugadores[i]=jugador
            multiplicador[3]= multiplicador[3]-5
    jugadores = ordenarJugadores(jugadores,opcion)
    return(jugadores)


# Asignacion de estadisticas:

# Titular:
def asignacionTitular(jugadores):
    jugadores = mejorarPotencial(jugadores,"ptitular")
    sistema = sistemasEquipo()
    for i in range(0,len(jugadores)):
        jugador = jugadores[i]
        # Portero
        if jugador["posicion"] == "Portero":
            if int(sistema[0]) > 0:
                jugador["titular"] = 1
                jugadores[i]=jugador
                sistema[0] = int(sistema[0]) -1
        # Defensa
        if jugador["posicion"] == "Defensa":
            if sistema[1] > 0:
                jugador["titular"] = 1
                jugadores[i]=jugador
                sistema[1] = int(sistema[1]) -1
        # Centrocampista
        if jugador["posicion"] == "Centrocampista":
            if sistema[2] > 0:
                jugador["titular"] = 1
                jugadores[i]=jugador
                sistema[2] = int(sistema[2]) -1
        # Delantero
        if jugador["posicion"] == "Delantero":
            if sistema[3] > 0:
                jugador["titular"] = 1
                jugadores[i]=jugador
                sistema[3] = int(sistema[3]) -1
    # jugadores = ordenarJugadores(jugadores,"titular")
    jugadores = jugadores[0:14] # Eliminamos a los jugadores que son suplentes y no van a salir
    return(jugadores)


# Asignar goles
def asignacionGoles(jugadores,goles):
    jugadores = mejorarPotencial(jugadores,"pasis")
    jugadores = mejorarPotencial(jugadores,"pgol")
    for i in range(0,goles):
        jugador = jugadores[0]
        jugador["gol"] = jugador["gol"]+1
        jugador["pgol"] = jugador["pgol"]-3
        jugadores[0] = jugador
        if (ra.randint(0,1)==1):
            jugadores2 = jugadores.pop(0) # Eliminamos el jugador que ha marcado gol
            print("Se genera una asistencia gol:",jugadores2)
            jugadores = asignacionAsistencias(jugadores)
            jugadores.append(jugadores2)
        jugadores = ordenarJugadores(jugadores,"pgol")
    return(jugadores)


def asignacionAsistencias(jugadores):
        jugadores = ordenarJugadores(jugadores,"pasis")
        jugador = jugadores[0]
        jugador["asis"] = jugador["asis"]+1
        jugador["pasis"] = jugador["pasis"]-4
        jugadores[0] = jugador
        return(jugadores)




jugadores=cs.selectJugadores(2)
jugadores = asignarProbabilidades(jugadores)
jugadores = asignacionTitular(jugadores)
jugadores = asignacionGoles(jugadores,5)
jugadores = ordenarJugadores(jugadores,"gol")
# print(jugadores)


for i in jugadores:
    jugador = i
    id = jugador["id"]
    posicion = jugador["posicion"]
    pgol = jugador["pgol"]
    titular = jugador["titular"]
    gol = jugador["gol"]
    pasis = jugador["pasis"]
    asis = jugador["asis"]

    print("Jugador: ", id," Posicion: ", posicion, " pgol: ", pgol, " gol: ",gol," titular: ", titular, " asis: ", asis)
