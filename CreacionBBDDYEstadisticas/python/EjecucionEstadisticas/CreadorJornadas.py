import sys
# in the sys.path list
sys.path.append('.\\')        
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



def calendario(jornada):
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
            fc.partido(fila1[t],fila2[t],jornada)
    else:
        print("El número de equipos no es par")
    


