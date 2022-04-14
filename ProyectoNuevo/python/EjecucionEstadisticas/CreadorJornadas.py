from numpy import append


def desplazamiento():
    print("hola")

def GenerarEquipos():
    numero=1
    fila1 =[]
    fila2 = []
    while ((numero % 2) != 0) :
        numero=int(input("Dime un número de equipos: "))
    numero2=int(numero/2)
    for i in range(numero2):
        fila1.append(i)
    for i in range(numero2,numero):
        fila2.append(i)
    print("jornada" ,1)
    print(fila1)
    print(fila2)
    for i in range(numero2):
        last=fila1.pop()
        first=fila2.pop(0)
        fila2.append(last)
        fila1.insert(1,first)
        print("jornada" ,i+2)
        print(fila1)
        print(fila2)
GenerarEquipos()

