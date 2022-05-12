import sys
sys.path.append('ProyectoLiga\ProyectoLigaInventada\ProyectoNuevo\python\webscraping')
import conexionsql as cs
import CreadorJornadas as cj
from time import sleep
# for i in range(18):
#     jornada = cs.selectJornada()
#     cj.calendario(jornada) 


jornada = cs.selectJornada()
sleep(2)
cj.calendario(jornada) 
