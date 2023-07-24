import sys 
import random
import os
# Obtén la ruta del directorio padre
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Agrega el directorio padre al sys.path
sys.path.append(parent_dir)
    
import conexionsql as cs
import funcionClub as fc
from time import sleep
def CalendarioNoconectado():
    # Escogemos un valor predeterminado para el numero de equipos
    numero=1
    # Definimos las listas donde se guardaran los equipos
    fila1 =[]
    fila2 = []
    # Si el numero de equipos es impar se sigue ejecutando el bucle
    while ((numero % 2) != 0) :
        # pedimos el número de equipos
        numero=int(input("Dime un número de equipos: "))
    # definimos el numero de encuentros y las jornadas
    numero2=int(numero/2)
    # Durante el rango del 1 a la mitad de equipos 
    for i in range(numero2):
        fila1.append(i+1)
    # Durante el rango de la mitad de equipos hasta el final
    for i in range(numero2,numero):
        fila2.append(i+1)
    print("jornada" ,1)
    print(fila1)
    print(fila2)
    for i in range(2,((numero*2)-2)):
        last=fila1.pop()
        first=fila2.pop(0)
        fila2.append(last)
        fila1.insert(1,first)
        print("jornada" ,i)
        print(fila1)
        print(fila2)
# Calendario()



def calendario_old(jornada):
     # Definimos las listas donde se guardaran los equipos
    fila1 =[]
    fila2 = []
    equipos=cs.selectActivoClub()
    if len(equipos)%2==0:
        mitad = int(len(equipos)/2)
        fila1.extend(equipos[:mitad])
        fila2.extend(equipos[int(mitad):int(mitad+mitad)])
        for i in range(1,jornada): 
            if jornada == 1:
                break
            last=fila1.pop()
            first=fila2.pop(0)
            fila2.append(last)
            fila1.insert(1,first)
        # print("jornada" ,jornada)
        for t in range(0,len(fila1)):
            # print(fila1[t], " VS ", fila2[t])
            sleep(1)
            # fc.partido(fila1[t],fila2[t],jornada)
    else:
        print("El número de equipos no es par")
    




def organizar_orden_temporada(temporada):
    equipos=cs.selectActivoClub()
    if len(equipos)%2==0:
        if temporada != 2:
            random.shuffle(equipos)

        for index in range(len(equipos)):
            cs.insertarOrdenTemporada(equipos[index],index,temporada)
    else:
        print("El número de equipos no es par")


def partidos_jornada(jornada):
    partidos=cs.select_calendario(jornada)
    for partido in partidos:
            fc.partido(partido["id_local"],partido["id_visitante"],jornada)




def calendario(jornada,temporada):
     # Definimos las listas donde se guardaran los equipos
    fila1 =[]
    fila2 = []
    equipos=cs.selectOrdenTemporada()
    if len(equipos)%2==0:
        mitad = int(len(equipos)/2)
        fila1.extend(equipos[:mitad])
        fila2.extend(equipos[int(mitad):int(mitad+mitad)])
        for i in range(1,jornada): 
            if jornada == 1:
                break
            last=fila1.pop()
            first=fila2.pop(0)
            fila2.append(last)
            fila1.insert(1,first)
        print("jornada" ,jornada)
        for t in range(0,len(fila1)):
            if jornada%2==0: #Local e2
                # print(fila2[t], " VS ", fila1[t])
                cs.insertarCalendario(fila2[t],fila1[t],jornada,temporada)
            else:
                # print(fila1[t], " VS ", fila2[t])
                cs.insertarCalendario(fila1[t],fila2[t],jornada,temporada)
            sleep(1)
            # fc.partido(fila1[t],fila2[t],jornada)
    else:
        print("El número de equipos no es par")




def generar_calendario(temporada):
    # Borramos los datos posibles que haya de esa temporada en el registro de orden
    cs.borrarOrdenTemporadaPorTemporada(temporada)
    cs.borrarCalendarioPorTemporada(temporada)
    # Organizamos el orden de la temporada:
    organizar_orden_temporada(temporada)
    
    # Definimos el calendario de la temporada con el siguiente bucle:
    for i in range(1,38):
        calendario(i,temporada)


