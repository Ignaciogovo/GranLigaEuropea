# Uso de beatiful soup para sacar datos de la liga
from bs4 import BeautifulSoup
import requests
import time
import sofifa

# link pagina:
def EjecucionPremier_original():
    url = "https://www.premierleague.com/tables"
    page = requests.get(url) # Optenemos la pagina
    soup = BeautifulSoup(page.content,'html.parser')
    prueba = soup.find_all("span", class_="long")
    equipos = list()
    count = 0
    pais = "Inglaterra"
    for i in prueba:
        if count == 20:
            break
        count +=1
        equipos.append(i.text) # Cogemos solo el texto de la etiqueta span
    for i in range(0,10):
        if equipos[i] in fundadores:
            continue
        else:
            print("puesto: %d equipo: %s" % (i+1, equipos[i]))
            sofifa.busquedajugadores(equipos[i],pais)
            break
            

def EjecucionPremier(year):
    url = "https://www.besoccer.com/competition/table/premier_league/"+str(year)
    page = requests.get(url) # Optenemos la pagina
    soup = BeautifulSoup(page.content,'html.parser')
    nombre_equipo = soup.find_all("span", class_="team-name")
    equipos = list()
    count = 0
    pais = "Inglaterra"
    for i in nombre_equipo:
        if count == 20:
            break
        count +=1
        equipo = i.text
        # Quitamos los espacios Al principio y al final
        equipo = equipo.strip()
        equipos.append(equipo) # Cogemos solo el texto de la etiqueta span
        print(equipo)
    for i in range(0,10):
        if equipos[i] in fundadores:
            continue
        else:
            print("puesto: %d equipo: %s" % (i+1, equipos[i]))
            # sofifa.busquedajugadores(equipos[i],pais)
            break




fundadores = ["Man. City","Liverpool","Chelsea","Arsenal","Tottenham Hotspur","Man. Utd"]
# fundadores = ["Manchester City","Liverpool","Chelsea","Arsenal","Tottenham Hotspur","Manchester United"]
