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
        temporada = cs.selectTemporada()
        if jornada == 1:
            print("Comienzo de la temporada", temporada)
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
        # Escritura del nombre de la copia de seguridad para la ejecución del comando en bash
        # newdata="LJ"+str(jornada)+"T"+str(temporada)+".sql"
        # with open('\\CreacionBBDDYEstadisticas\\backup\\jornadaTemporada.txt', "w") as myfile:
        #     myfile.write(newdata)
else:
    print("Lo siento, la temporada aún no ha Empezado")
    
now = datetime.now()
print(now)