# importing the sys module
import sys
# in the sys.path list
sys.path.append('.\\')        
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
def sistemasEquipo(jugadores):
    sistema = ra.randint(0,4)
    if sistema==0 or sistema == 1:
        sistema = [1,4,4,2]
    if sistema==2:
        sistema = [1,4,3,3]
    if sistema==3:
        sistema = [1,5,3,2]   
    if sistema==4:
        sistema = [1,4,5,1]
# Para evitar problemas con equipos que tienen menos de 3 delanteros:
    contador = 0
    for i in range(0,len(jugadores)):
        if (jugadores[i])["posicion"] == "Delantero":
            contador=contador+1
    if contador < 3:
        sistema = [1,4,5,1]
    return(sistema)
# Calculo total de tarjetas de un equipo
def tarjetasTotales():
    amarillas = ra.randrange(0,5)
    rojas=int((ra.randrange(0,3)*ra.randrange(0,4))/3)
    if rojas < 1:
        rojas = 0
    tarjetas=[amarillas,rojas]
    return(tarjetas)

def asignarProbabilidades(jugadores,id_club):
    #Sacamos el id del partido anterior para hacer comprobaciones
    id_partido = cs.selectIdPartidoClub(id_club)
    eliminacion = []
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
        #Comprobamos si ha tenido una roja o dos amarillas en el partido anterior
        tarjetas = cs.selectRojasAmarillas((jugadores[i])["id"],id_partido)
        if tarjetas[0]>1 or tarjetas[1] > 0:
            eliminacion.append(jugadores[i])
    for i in range(0,len(eliminacion)):
        eliminado = eliminacion[i]
        jugadores.remove(eliminado)
    return(jugadores)


def mejorarPotencial(jugadores,opcion):
    #Multiplicadores
    if opcion == "ptitular":
        multiplicador = [10,35,35,35]
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
    sistema = sistemasEquipo(jugadores)
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
    jugadores = ordenarJugadores(jugadores,"titular")
    jugadores = jugadores[0:14] # Eliminamos a los jugadores que son suplentes y no van a salir
    return(jugadores)


# Asignar goles
def asignacionGoles(jugadores,goles):
    # Ordenamos por valor para mejorar el potencial de asistencias según el valor del jugador
    jugadores = ordenarJugadores(jugadores,"valor")
    jugadores = mejorarPotencial(jugadores,"pasis")
    # Ordenamos por valor para mejorar el potencial de gol según el valor del jugador
    jugadores = ordenarJugadores(jugadores,"valor")
    jugadores = mejorarPotencial(jugadores,"pgol")
    for i in range(0,goles):
        jugador = jugadores[0]
        jugador["gol"] = jugador["gol"]+1
        jugador["pgol"] = jugador["pgol"]-3
        jugadores[0] = jugador
        if (ra.randint(0,1)==1):
            
            jugadores2 = jugadores.pop(0) # Eliminamos el jugador que ha marcado gol
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

def asignacionTarjetas(jugadores):
    jugadores = mejorarPotencial(jugadores,"proja")
    jugadores = mejorarPotencial(jugadores,"pamarilla")
    tarjetas=tarjetasTotales()
    amarillas = tarjetas[0]
    rojas = tarjetas[1]
    for i in range(0,amarillas):
        jugador = jugadores[0]
        # Condicion si jugador tiene 2 amarillas
        if jugador["amarilla"]>=2:
            i = i-1
            jugador["pamarilla"] = 0
        else:
            jugador["amarilla"] = jugador["amarilla"]+1
            jugador["pamarilla"] = jugador["pamarilla"]-5
        jugadores[0] = jugador
        jugadores=ordenarJugadores(jugadores,"pamarilla")
    jugadores=ordenarJugadores(jugadores,"proja")
    for i in range(0,rojas):
        jugador = jugadores[0]
        # Condicion si jugador tiene 1 roja
        if jugador["roja"]>=1 or jugador["amarilla"] >=2:
            i = i-1
            jugador["proja"] = 0
        else:
            jugador["roja"] = jugador["roja"]+1
            jugador["proja"] = 0
        jugadores[0] = jugador
        jugadores=ordenarJugadores(jugadores,"proja")
    return(jugadores)

def insertarEstadisticas(jugadores):
    id_partido = cs.selectPartido()
    for i in jugadores:
        jugador = i
        id = jugador["id"]
        titular = jugador["titular"]
        gol = jugador["gol"]
        asis = jugador["asis"]
        rojas = jugador["roja"]
        amarilla = jugador["amarilla"]
        datos = [id,id_partido,gol,asis,amarilla,rojas,titular]
        cs.insertarEstadisticasPartidos(datos)

def ejecucionEstadisticas(club,gol):
    jugadores=cs.selectJugadores(club)
    jugadores = asignarProbabilidades(jugadores,club)
    jugadores = asignacionTitular(jugadores)
    jugadores = asignacionGoles(jugadores,gol)
    jugadores = asignacionTarjetas(jugadores)
    jugadores = ordenarJugadores(jugadores,"titular")
    insertarEstadisticas(jugadores)



def comprobaciones(jugadores,opcion,opcion2):
    for i in jugadores:
        jugador = i
        print("Jugador: ", jugador["id"], " posicion: ", jugador["posicion"], "Valor:",jugador["valor"])
        print("Opcion: " ,opcion , " ",jugador[opcion])
        if opcion2 != 0:
            print("Opcion2 :", opcion2, " ", jugador[opcion2])
        print("   ")