import sys
sys.path.append('ProyectoLiga\ProyectoLigaInventada\ProyectoNuevo\python\webscraping')
import conexionsql as cs
import CreadorJornadas as cj

jornada = cs.selectJornada()
cj.calendario(jornada) 
