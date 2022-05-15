import conexionsql as cs
import conexiontwitter as ct
import CreadorJornadas as cj
from time import sleep
# for i in range(18):
#     jornada = cs.selectJornada()
#     cj.calendario(jornada) 


jornada = cs.selectJornada()
ct.twittearJornada(jornada)
sleep(2)
cj.calendario(jornada) 
