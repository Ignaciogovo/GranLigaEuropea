from bs4 import BeautifulSoup
import requests
import time
import sofifa





# Busqueda clasificación:
def Busqueda_clasificacion(year,url,fundadores,pais):
    url = url+str(year)
    page = requests.get(url) # Optenemos la pagina
    soup = BeautifulSoup(page.content,'html.parser')
    nombre_equipo = soup.find_all("span", class_="team-name")
    equipos = list()
    count = 0
    for i in nombre_equipo:
        if count == 20:
            break
        count +=1
        equipo = i.text
        # Quitamos los espacios Al principio y al final
        equipo = equipo.strip()
        equipos.append(equipo) # Cogemos solo el texto de la etiqueta span
    for i in range(0,10):
        if equipos[i] in fundadores:
            continue
        else:
            print("puesto: %d equipo: %s" % (i+1, equipos[i]))
            sofifa.busquedajugadores(equipos[i],pais)
            break