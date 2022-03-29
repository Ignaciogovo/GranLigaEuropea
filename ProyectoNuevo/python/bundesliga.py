from bs4 import BeautifulSoup
import requests
import time
import sofifa
# link pagina:

def EjecucionBundesliga():
    url = "https://www.bundesliga.com/es/bundesliga/clasificacion"
    page = requests.get(url) # Optenemos la pagina
    soup = BeautifulSoup(page.content,'html.parser')
    prueba = soup.find_all("td", class_="team")
    equipos = list()
    count = 0
    pais = "Alemania"
    for i in prueba:
        if count == 20:
            break
        count +=1
        Sininiciales= (i.text)[3:]
        Sininiciales ='' .join(unique_list(Sininiciales.split()))
        equipos.append(Sininiciales) # Cogemos solo el texto de la etiqueta span
    for i in range(0,10):
        print("puesto: %d equipo: %s" % (i+1, equipos[i]))
        sofifa.busquedajugadores(equipos[i],pais)

#Eliminar palabras repetidas
# Obtenido desde: https://foroayuda.es/como-eliminar-palabras-duplicadas-de-la-cadena-en-el-ejemplo-de-codigo-de-python/
def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist