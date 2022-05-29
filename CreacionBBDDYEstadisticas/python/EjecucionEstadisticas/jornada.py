# importing the sys module
import sys
# in the sys.path list
sys.path.append('.\\')     
import conexionsql as cs
import conexiontwitter as ct
import CreadorJornadas as cj
from time import sleep
from datetime import datetime


def finalizarTemporada():
    # Finalizamos temporada
    cs.finalizarTemporada()
    # desactivamos a los jugadores y club
    cs.AnularActivoJugadores()
    cs.AnularActivoClub()

#fecha actual
jornada = cs.selectJornada()
if jornada > 0:
    if jornada > 38:
        print("La temporada ha terminado, debes iniciar una temporada")
    else:
        print("Comienzo de jornada: ",jornada)
        now = datetime.now()
        print(now)
        # ct.twittearJornada(jornada)
        sleep(2)
        cj.calendario(jornada)
        print("Finalización de jornada", jornada)

        if jornada == 38:
            print("Finalización de temporada")
            finalizarTemporada()
            # ct.twittearFinal()
else:
    print("Lo siento, la temporada aún no ha Empezado")
    
now = datetime.now()
print(now)
