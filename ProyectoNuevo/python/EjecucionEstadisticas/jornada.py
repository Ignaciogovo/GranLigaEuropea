from ast import If
from re import X
import conexionsql as cs
import conexiontwitter as ct
import CreadorJornadas as cj
from time import sleep
# for i in range(18):
#     jornada = cs.selectJornada()
#     cj.calendario(jornada) 

jornada = cs.selectJornada()
if jornada > 0:
    if jornada > 38:
        print("La temporada ha terminado, debes iniciar una temporada")
    else:
        ct.twittearJornada(jornada)
        sleep(2)
        cj.calendario(jornada) 
else:
    print("Lo siento, la temporada aún no ha Empezado")