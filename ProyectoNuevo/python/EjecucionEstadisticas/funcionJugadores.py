from cgi import print_arguments
import sys

from pandas import array
sys.path.append('ProyectoLiga\ProyectoLigaInventada\ProyectoNuevo\python\webscraping')
import conexionsql as cs
import random as ra


def ordenarJugadores(array,key):
    for i in range(0,len(array)):
        for a in range(i+1,len(array)):
            numero1 = array[i]
            numero2 = array[a]
            if (numero2[key]>numero1[key]):
                    intermedio = numero2
                    array[a] = array[i]
                    array[i] = intermedio
    return(array)
def asignarProbabilidades(jugadores):
    for i in range(0,len(jugadores)):
        ptitular = ra.randrange(0,11)
        titular = 0
        pgol = ra.randrange(0,11)
        gol = 0
        pamarilla = ra.randrange(0,11)
        proja = ra.randrange(0,11)
        pasis = ra.randrange(0,11)
        (jugadores[i])["ptitular"] = ptitular
        (jugadores[i])["titular"] = 0
        (jugadores[i])["pgol"] = pgol
        (jugadores[i])["gol"] = 0
        (jugadores[i])["pamarilla"] = pamarilla
        (jugadores[i])["amarilla"] = 0
        (jugadores[i])["proja"] = proja
        (jugadores[i])["roja"] = 0
        (jugadores[i])["pasis"] = pasis
        (jugadores[i])["asis"] = 0
    return(jugadores)

jugadores=cs.selectJugadores(2)
jugadores = asignarProbabilidades(jugadores)
jugadores = ordenarJugadores(jugadores,"pgol")
print(jugadores)
