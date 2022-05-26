from ast import If
from re import X
import conexionsql as cs
import conexiontwitter as ct
import CreadorJornadas as cj
from time import sleep
from datetime import datetime

#fecha actual
now = datetime.now()
print(now)
jornada = cs.selectJornada()
if jornada > 0:
    if jornada > 38:
        print("La temporada ha terminado, debes iniciar una temporada")
    else:
        print("Comienzo de jornada: ",jornada)
        # ct.twittearJornada(jornada)
        sleep(2)
        cj.calendario(jornada)
        print("Finalización de jornada", jornada)
else:
    print("Lo siento, la temporada aún no ha Empezado")
now = datetime.now()
print(now)