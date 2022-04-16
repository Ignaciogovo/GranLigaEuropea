import sys
sys.path.append('ProyectoLiga\ProyectoLigaInventada\ProyectoNuevo\python\webscraping')
import CreadorJornadas as cj
import conexionsql as cs

def partido(e1,e2):
    v1 = cs.selectValorClub(e1)
    v2 = cs.selectValorClub(e2)
    