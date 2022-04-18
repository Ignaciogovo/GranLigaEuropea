import sys
sys.path.append('ProyectoLiga\ProyectoLigaInventada\ProyectoNuevo\python\webscraping')
import conexionsql as cs

def partido(e1,e2):
    v1 = cs.selectValorClub(e1)
    v2 = cs.selectValorClub(e2)
    diff = v1-v2
    print(diff)
partido(1,2)
    