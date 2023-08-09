from tempfile import TemporaryDirectory
import sys 
import os
# Obtén la ruta del directorio padre
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Agrega el directorio padre al sys.path
sys.path.append(parent_dir)
   
import conexionsql as cs
import conexiontwitter as ct
import random as ra
import funcionJugadores as fj

def partido(e_local,e_visitante,jornada):
    # Temporada
    temporada=  cs.selectTemporada()
    v_local = cs.selectValorClub(e_local)
    v_visitante = cs.selectValorClub(e_visitante)
    diff = abs(v_local-v_visitante)
    #Asignacion equipo ganador
    potenciales=calculoPotenciales(v_local,v_visitante,diff,jornada)
    potencial_local = potenciales["potencial_local"]
    potencial_visitante = potenciales["potencial_visitante"]
    aforo = potenciales["aforo"]
    # Asignar un rango para empates
    diff =abs(potencial_local-potencial_visitante)
    if diff <= 0.5:
        potencial_visitante = potencial_local

    # Asignacion de arbitro:
    arbitros=cs.select_id_arbitro_filtrado(jornada,temporada)
    arbitro= ra.choice(arbitros)[0]

    if potencial_local < potencial_visitante:
        #Ganador segundo equipo:
        #Asignacion de goles
        gol_local = int(round(potencial_local/2.5,0))
        gol_visitante = int(round(potencial_visitante/2.5,0))
        if gol_local == gol_visitante:
            gol_visitante=gol_visitante+1
    elif potencial_local > potencial_visitante:
        #Ganador primer equipo:
        #Asignacion de goles
        gol_local = int(round(potencial_local/2.5,0))
        gol_visitante = int(round(potencial_visitante/2.5,0))
        if gol_local == gol_visitante:
            gol_local=gol_local+1
    elif potencial_local==potencial_visitante:
        # Empate:
        gol_local = int(round(potencial_local/2.5,0))
        gol_visitante = gol_local
    datos_partidos= [e_local,e_visitante,gol_local,gol_visitante,arbitro,(str(aforo) + '%'),jornada,temporada]
    #Insertamos resultado del partido
    cs.insertarPartidos(datos_partidos)
    # ejecutamos las estadisticas de los jugadores
    fj.ejecucionEstadisticas(e_local,gol_local)
    fj.ejecucionEstadisticas(e_visitante,gol_visitante)
    # Actualizamos Clasificacion
    cs.updateclasificacion(e_local,gol_local,e_visitante,gol_visitante, temporada)
    # Twittear resultado de partido
    ct.twittearPartido(e_local,e_visitante,gol_local,gol_visitante)

# Calcula el potencial de victoria de cada equipo
def calculoPotenciales(v_local,v_visitante,diff,jornada):
    if v_local < v_visitante:
        if diff < 150000000:
            potencial_visitante= ra.randrange(9)
            potencial_local= ra.randrange(9)
            aforo = ra.randrange(70,100)
            # print("Potencial minimo")
        elif diff >= 150000000 and diff < 200000000:
            potencial_visitante= 1.15*ra.randrange(9)
            potencial_local= ra.randrange(9)
            aforo = ra.randrange(70,95)
            # print("Potencial entre 1500000 y 20000")

        elif diff >= 200000000 and diff < 300000000:
            potencial_visitante= 1.35*ra.randrange(9)
            potencial_local= ra.randrange(9)
            aforo = ra.randrange(65,96)
            # print("Potencial entre 200000 y 30000")

        elif diff >= 300000000 and diff < 600000000:
            potencial_visitante= 1.55*ra.randrange(9)
            potencial_local= ra.randrange(9)
            aforo = ra.randrange(65,91)
            # print("Potencial entre 3000000 y 6000000")

        elif diff >= 600000000:
            potencial_visitante= 1.75*ra.randrange(9)
            potencial_local= ra.randrange(9)
            aforo = ra.randrange(65,100)
            # print("Mayor potencial")

    elif v_local > v_visitante:
        if diff < 150000000:
            potencial_local= ra.randrange(9)
            potencial_visitante= ra.randrange(9)
            aforo = ra.randrange(70,100)
            # print("Potencial minimo")
        elif diff >= 150000000 and diff < 200000000:
            potencial_local= 1.15*ra.randrange(9)
            potencial_visitante= ra.randrange(9)
            aforo = ra.randrange(70,95)
            # print("Potencial entre 1500000 y 20000")
        elif diff >= 200000000 and diff < 300000000:
            potencial_local= 1.35*ra.randrange(9)
            potencial_visitante= ra.randrange(9)
            aforo = ra.randrange(65,96)
            # print("Potencial entre 200000 y 30000")
        elif diff >= 300000000 and diff < 600000000:
            potencial_local= 1.55*ra.randrange(9)
            potencial_visitante= ra.randrange(9)
            aforo = ra.randrange(65,91)
            # print("Potencial entre 3000000 y 6000000")
        elif diff >= 600000000:
            potencial_local= 1.75*ra.randrange(9)
            potencial_visitante= ra.randrange(9)
            aforo = ra.randrange(65,100)
            # print("Mayor potencial")
    elif v_local == v_visitante:
        # print("Iguales")
        potencial_local= ra.randrange(9)
        potencial_visitante= ra.randrange(9)
        aforo = ra.randrange(70,100)
    # Ventaja local
    if aforo >=80:
        if jornada%2==0:
            potencial_visitante=potencial_visitante*1.15
        else:
            potencial_local=potencial_local*1.15
    # Incluir datos obtenidos en un diccionario
    datos = {}
    datos["potencial_local"] =potencial_local
    datos["potencial_visitante"] = potencial_visitante
    datos["aforo"] = aforo
    return(datos)