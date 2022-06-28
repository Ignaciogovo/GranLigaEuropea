from tempfile import TemporaryDirectory
# importing the sys module
import sys
# in the sys.path list
sys.path.append('.\\')        
import conexionsql as cs
import conexiontwitter as ct
import random as ra
import funcionJugadores as fj

def partido(e1,e2,jornada):
    v1 = cs.selectValorClub(e1)
    v2 = cs.selectValorClub(e2)
    diff = abs(v1-v2)
    #Asignacion equipo ganador
    potenciales=calculoPotenciales(v1,v2,diff,jornada)
    potencial1 = potenciales["potencial1"]
    potencial2 = potenciales["potencial2"]
    aforo = potenciales["aforo"]
    # Asignar un rango para empates
    diff =abs(potencial1-potencial2)
    if diff <= 0.5:
        potencial2 = potencial1
    # Asignacion de arbitro:
    arbitro= ra.randint(1,9)
    # Temporada
    temporada=  cs.selectTemporada()
    if potencial1 < potencial2:
        #Ganador segundo equipo:
        #Asignacion de goles
        gol1 = int(round(potencial1/2.5,0))
        gol2 = int(round(potencial2/2.5,0))
        if gol1 == gol2:
            gol2=gol2+1
        if jornada%2==0: #Local e2
            datos_partidos= [e2,e1,gol2,gol1,arbitro,(str(aforo) + '%'),jornada,temporada]
            #Insertamos resultado del partido
            cs.insertarPartidos(datos_partidos)
            # ejecutamos las estadisticas de los jugadores
            fj.ejecucionEstadisticas(e1,gol1)
            fj.ejecucionEstadisticas(e2,gol2)
            # Actualizamos Clasificacion
            cs.updateclasificacion(e2,gol2,e1, gol1, temporada)
            # Twittear resultado de partido
            ct.twittearPartido(e2,e1,gol2,gol1)
        else: #Local e1
            datos_partidos= [e1,e2,gol1,gol2,arbitro,(str(aforo) + '%'),jornada,temporada]
            #Insertamos resultado del partido
            cs.insertarPartidos(datos_partidos)
            # ejecutamos las estadisticas de los jugadores
            fj.ejecucionEstadisticas(e1,gol1)
            fj.ejecucionEstadisticas(e2,gol2)
            # Actualizamos Clasificacion
            cs.updateclasificacion(e1,gol1,e2,gol2,temporada)
            # Twittear resultado de partido
            ct.twittearPartido(e1,e2,gol1,gol2)
    elif potencial1 > potencial2:
        #Ganador primer equipo:
        #Asignacion de goles
        gol1 = int(round(potencial1/2.5,0))
        gol2 = int(round(potencial2/2.5,0))
        if gol1 == gol2:
            gol1=gol1+1
        if jornada%2==0: #Local e2
            datos_partidos= [e2,e1,gol2,gol1,arbitro,(str(aforo) + '%'),jornada,temporada]
            #Insertamos resultado del partido
            cs.insertarPartidos(datos_partidos)
            # ejecutamos las estadisticas de los jugadores
            fj.ejecucionEstadisticas(e1,gol1)
            fj.ejecucionEstadisticas(e2,gol2)
            # Actualizamos Clasificacion
            cs.updateclasificacion(e2,gol2,e1, gol1, temporada)
            # Twittear resultado de partido
            ct.twittearPartido(e2,e1,gol2,gol1)
        else: #Local e1
            datos_partidos= [e1,e2,gol1,gol2,arbitro,(str(aforo) + '%'),jornada,temporada]
            #Insertamos resultado del partido
            cs.insertarPartidos(datos_partidos)
            # ejecutamos las estadisticas de los jugadores
            fj.ejecucionEstadisticas(e1,gol1)
            fj.ejecucionEstadisticas(e2,gol2)
            # Actualizamos Clasificacion
            cs.updateclasificacion(e1,gol1,e2,gol2, temporada)
            # Twittear resultado de partido
            ct.twittearPartido(e1,e2,gol1,gol2)
    elif potencial1==potencial2:
        # Empate:
        gol1 = int(round(potencial1/2.5,0))
        gol2 = gol1
        if jornada%2==0: #Local e2
            datos_partidos= [e2,e1,gol2,gol1,arbitro,(str(aforo) + '%'),jornada,temporada]
            #Insertamos resultado del partido
            cs.insertarPartidos(datos_partidos)
            # ejecutamos las estadisticas de los jugadores
            fj.ejecucionEstadisticas(e1,gol1)
            fj.ejecucionEstadisticas(e2,gol2)
            # Actualizamos Clasificacion
            cs.updateclasificacion(e2,gol2,e1, gol1, temporada)
            # Twittear resultado de partido
            ct.twittearPartido(e2,e1,gol2,gol1)
        else: #Local e1
            datos_partidos= [e1,e2,gol1,gol2,arbitro,(str(aforo) + '%'),jornada,temporada]
            #Insertamos resultado del partido
            cs.insertarPartidos(datos_partidos)
            # ejecutamos las estadisticas de los jugadores
            fj.ejecucionEstadisticas(e1,gol1)
            fj.ejecucionEstadisticas(e2,gol2)
            # Actualizamos Clasificacion
            cs.updateclasificacion(e1,gol1,e2,gol2, temporada)
            # Twittear resultado de partido
            ct.twittearPartido(e1,e2,gol1,gol2)

# Calcula el potencial de victoria de cada equipo
def calculoPotenciales(v1,v2,diff,jornada):
    if v1 < v2:
        if diff < 150000000:
            potencial2= ra.randrange(9)
            potencial1= ra.randrange(9)
            aforo = ra.randrange(70,100)
            # print("Potencial minimo")
        elif diff >= 150000000 and diff < 200000000:
            potencial2= 1.15*ra.randrange(9)
            potencial1= ra.randrange(9)
            aforo = ra.randrange(70,95)
            # print("Potencial entre 1500000 y 20000")

        elif diff >= 200000000 and diff < 300000000:
            potencial2= 1.35*ra.randrange(9)
            potencial1= ra.randrange(9)
            aforo = ra.randrange(65,96)
            # print("Potencial entre 200000 y 30000")

        elif diff >= 300000000 and diff < 600000000:
            potencial2= 1.55*ra.randrange(9)
            potencial1= ra.randrange(9)
            aforo = ra.randrange(65,91)
            # print("Potencial entre 3000000 y 6000000")

        elif diff >= 600000000:
            potencial2= 1.75*ra.randrange(9)
            potencial1= ra.randrange(9)
            aforo = ra.randrange(65,100)
            # print("Mayor potencial")

    elif v1 > v2:
        if diff < 150000000:
            potencial1= ra.randrange(9)
            potencial2= ra.randrange(9)
            aforo = ra.randrange(70,100)
            # print("Potencial minimo")
        elif diff >= 150000000 and diff < 200000000:
            potencial1= 1.15*ra.randrange(9)
            potencial2= ra.randrange(9)
            aforo = ra.randrange(70,95)
            # print("Potencial entre 1500000 y 20000")
        elif diff >= 200000000 and diff < 300000000:
            potencial1= 1.35*ra.randrange(9)
            potencial2= ra.randrange(9)
            aforo = ra.randrange(65,96)
            # print("Potencial entre 200000 y 30000")
        elif diff >= 300000000 and diff < 600000000:
            potencial1= 1.55*ra.randrange(9)
            potencial2= ra.randrange(9)
            aforo = ra.randrange(65,91)
            # print("Potencial entre 3000000 y 6000000")
        elif diff >= 600000000:
            potencial1= 1.75*ra.randrange(9)
            potencial2= ra.randrange(9)
            aforo = ra.randrange(65,100)
            # print("Mayor potencial")
    elif v1 == v2:
        # print("Iguales")
        potencial1= ra.randrange(9)
        potencial2= ra.randrange(9)
        aforo = ra.randrange(70,100)
    # Ventaja local
    if aforo >=80:
        if jornada%2==0:
            potencial2=potencial2*1.15
        else:
            potencial1=potencial1*1.15
    # Incluir datos obtenidos en un diccionario
    datos = {}
    datos["potencial1"] =potencial1
    datos["potencial2"] = potencial2
    datos["aforo"] = aforo
    return(datos)