from cgi import print_arguments
import sys
sys.path.append('ProyectoLiga\ProyectoLigaInventada\ProyectoNuevo\python\webscraping')
import conexionsql as cs
import random as ra

def partido(e1,e2,jornada):
    v1 = cs.selectValorClub(e1)
    v2 = cs.selectValorClub(e2)
    diff = v1-v2
    diff = abs(diff)
    #Asignacion equipo ganador
    potenciales=calculoPotenciales(v1,v2,diff,jornada)
    potencial1 = potenciales["potencial1"]
    potencial2 = potenciales["potencial2"]
    aforo = potenciales["aforo"]
    # Asignacion de arbitro:
    arbitro= ra.randrange(1,9)
    # Temporada
    temporada=  cs.selectTemporada()
    if potencial1 < potencial2:
        #Ganador segundo equipo:
        #Asignacion de goles
        gol1 = int(round(potencial1/2.5,0))
        gol2 = int(round(potencial2/2.5,0))
        if gol1 == gol2:
            gol2=gol2+1
        # print("Gana segundo equipo con:")
        # print(gol2, "Goles")
        # print("Pierde primer equipo con:")
        # print(gol1, "Goles")
        # print("El aforo ha sido de:", aforo, "%")
        if jornada%2==0:
            datos_partidos= [e2,e1,gol2,gol1,arbitro,(str(aforo) + '%'),jornada,temporada]
            cs.insertarPartidos(datos_partidos)
        else:
            datos_partidos= [e1,e2,gol1,gol2,arbitro,(str(aforo) + '%'),jornada,temporada]
            cs.insertarPartidos(datos_partidos)
    elif potencial1 > potencial2:
        #Ganador primer equipo:
        #Asignacion de goles
        gol1 = int(round(potencial1/2.5,0))
        gol2 = int(round(potencial2/2.5,0))
        if gol1 == gol2:
            gol1=gol1+1
        # print("Gana primer equipo con:")
        # print(gol1, "Goles")
        # print("Pierde segundo equipo con:")
        # print(gol2, "Goles")
        # print("El aforo ha sido de:", aforo, "%")
        if jornada%2==0:
            datos_partidos= [e2,e1,gol2,gol1,arbitro,(str(aforo) + '%'),jornada,temporada]
            cs.insertarPartidos(datos_partidos)
        else:
            datos_partidos= [e1,e2,gol1,gol2,arbitro,(str(aforo) + '%'),jornada,temporada]
            cs.insertarPartidos(datos_partidos)
    elif potencial1==potencial2:
        # Empate:
        gol1 = int(round(potencial1/2.5,0))
        gol2 = gol1
        print("Empate a ", gol2, "Goles")
        print("El aforo ha sido de:", aforo, "%")
        if jornada%2==0:
            datos_partidos= [e2,e1,gol2,gol1,arbitro,(str(aforo) + '%'),jornada,temporada]
            cs.insertarPartidos(datos_partidos)
        else:
            datos_partidos= [e1,e2,gol1,gol2,arbitro,(str(aforo) + '%'),jornada,temporada]
            cs.insertarPartidos(datos_partidos)

# Calcula el potencial de victoria de cada equipo
def calculoPotenciales(v1,v2,diff,jornada):
    if v1 < v2:
        if diff < 150000000:
            potencial2= ra.randrange(9)
            potencial1= ra.randrange(9)
            aforo = ra.randrange(70,100)
            # print("Potencial minimo")
        elif diff >= 150000000 and diff < 200000000:
            potencial2= 1.15*ra.randrange(9)
            potencial1= ra.randrange(9)
            aforo = ra.randrange(70,95)
            # print("Potencial entre 1500000 y 20000")

        elif diff >= 200000000 and diff < 300000000:
            potencial2= 1.35*ra.randrange(9)
            potencial1= ra.randrange(9)
            aforo = ra.randrange(65,96)
            # print("Potencial entre 200000 y 30000")

        elif diff >= 300000000 and diff < 600000000:
            potencial2= 1.55*ra.randrange(9)
            potencial1= ra.randrange(9)
            aforo = ra.randrange(65,91)
            # print("Potencial entre 3000000 y 6000000")

        elif diff >= 600000000:
            potencial2= 1.75*ra.randrange(9)
            potencial1= ra.randrange(9)
            aforo = ra.randrange(65,100)
            # print("Mayor potencial")

    elif v1 > v2:
        if diff < 150000000:
            potencial1= ra.randrange(9)
            potencial2= ra.randrange(9)
            aforo = ra.randrange(70,100)
            # print("Potencial minimo")
        elif diff >= 150000000 and diff < 200000000:
            potencial1= 1.15*ra.randrange(9)
            potencial2= ra.randrange(9)
            aforo = ra.randrange(70,95)
            # print("Potencial entre 1500000 y 20000")
        elif diff >= 200000000 and diff < 300000000:
            potencial1= 1.35*ra.randrange(9)
            potencial2= ra.randrange(9)
            aforo = ra.randrange(65,96)
            # print("Potencial entre 200000 y 30000")
        elif diff >= 300000000 and diff < 600000000:
            potencial1= 1.55*ra.randrange(9)
            potencial2= ra.randrange(9)
            aforo = ra.randrange(65,91)
            # print("Potencial entre 3000000 y 6000000")
        elif diff >= 600000000:
            potencial1= 1.75*ra.randrange(9)
            potencial2= ra.randrange(9)
            aforo = ra.randrange(65,100)
            # print("Mayor potencial")
    elif v1 == v2:
        # print("Iguales")
        potencial1= ra.randrange(9)
        potencial2= ra.randrange(9)
        aforo = ra.randrange(70,100)
    # Ventaja local
    if aforo >=80:
        if jornada%2==0:
            potencial2=potencial2*1.15
        else:
            potencial1=potencial1*1.15
    # Incluir datos obtenidos en un diccionario
    datos = {}
    datos["potencial1"] =potencial1
    datos["potencial2"] = potencial2
    datos["aforo"] = aforo
    return(datos)

# for i in range(1,19):
    # partido(i,i+1)


# partido(6,9,1)
# partido(6,11,12)





# #media = sum(prueba)/len(prueba)
# print (prueba)
 


# Diferencia entre manchester city y marsella : 877.315.000
# Diferencia entre manchester city y AC Milan : 593.690.000