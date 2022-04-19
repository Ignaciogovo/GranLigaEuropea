from cgi import print_arguments
import sys
sys.path.append('ProyectoLiga\ProyectoLigaInventada\ProyectoNuevo\python\webscraping')
import conexionsql as cs
import random as ra

def partido(e1,e2):
    v1 = cs.selectValorClub(e1)
    v2 = cs.selectValorClub(e2)
    diff = v1-v2
    diff = abs(diff)
    print(diff)
    if v1 < v2:
        print("Mayor potencial " ,e2)
        if diff < 150000000:
            potencial2= ra.randrange(9)
            potencial1= ra.randrange(9)
            aforo = ra.randrange(70,100)
            print("Potencial minimo")
        elif diff >= 150000000 and diff < 200000000:
            potencial2= 1.15*ra.randrange(9)
            potencial1= ra.randrange(9)
            aforo = ra.randrange(70,95)
            print("Potencial entre 1500000 y 20000")

        elif diff >= 200000000 and diff < 300000000:
            potencial2= 1.35*ra.randrange(9)
            potencial1= ra.randrange(9)
            aforo = ra.randrange(65,96)
            print("Potencial entre 200000 y 30000")

        elif diff >= 300000000 and diff < 600000000:
            potencial2= 1.55*ra.randrange(9)
            potencial1= ra.randrange(9)
            aforo = ra.randrange(65,91)
            print("Potencial entre 3000000 y 6000000")

        elif diff >= 600000000:
            potencial2= 1.75*ra.randrange(9)
            potencial1= ra.randrange(9)
            aforo = ra.randrange(65,100)
            print("Mayor potencial")

    elif v1 > v2:
        print("Mayor potencial " ,e1)
        if diff < 150000000:
            potencial1= ra.randrange(9)
            potencial2= ra.randrange(9)
            aforo = ra.randrange(70,100)
            print("Potencial minimo")
        elif diff >= 150000000 and diff < 200000000:
            potencial1= 1.15*ra.randrange(9)
            potencial2= ra.randrange(9)
            aforo = ra.randrange(70,95)
            print("Potencial entre 1500000 y 20000")
        elif diff >= 200000000 and diff < 300000000:
            potencial1= 1.35*ra.randrange(9)
            potencial2= ra.randrange(9)
            aforo = ra.randrange(65,96)
            print("Potencial entre 200000 y 30000")
        elif diff >= 300000000 and diff < 600000000:
            potencial1= 1.55*ra.randrange(9)
            potencial2= ra.randrange(9)
            aforo = ra.randrange(65,91)
            print("Potencial entre 3000000 y 6000000")
        elif diff >= 600000000:
            potencial1= 1.75*ra.randrange(9)
            potencial2= ra.randrange(9)
            aforo = ra.randrange(65,100)
            print("Mayor potencial")
    elif v1 == v2:
        print("Iguales")
        potencial1= ra.randrange(9)
        potencial2= ra.randrange(9)
        aforo = ra.randrange(70,100)


# for i in range(1,19):
    # partido(i,i+1)


partido(6,9)




# #media = sum(prueba)/len(prueba)
# print (prueba)
 


# Diferencia entre manchester city y marsella : 877.315.000
# Diferencia entre manchester city y AC Milan : 593.690.000