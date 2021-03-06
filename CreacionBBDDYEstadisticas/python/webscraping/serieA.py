from bs4 import BeautifulSoup
import requests
import time
import sofifa
# link pagina:
def EjecucionSerieA():
    url = "https://onefootball.com/es/competicion/serie-a-13/clasificacion"
    page = requests.get(url) # Optenemos la pagina
    soup = BeautifulSoup(page.content,'html.parser')
    nombre_equipo = soup.find_all("p", class_="title-7-medium standings__team-name")
    equipos = list()
    count = 0
    pais = "Italia"
    for i in nombre_equipo:
        if count == 20:
            break
        count +=1
        equipo = i.text
        # Quitamos los espacios Al principio y al final
        equipo = equipo.strip()
        # Personalizamos algunos nombre de los equipos para evitar posibles problemas en el scraping 
        if equipo == "Inter de Milán":
            equipo = "Inter"
        equipos.append(equipo) # Cogemos solo el texto de la etiqueta span
    for i in range(0,10):
        if equipos[i] in fundadores:
            continue
        else:
            print("puesto: %d equipo: %s" % (i+1, equipos[i]))
            sofifa.busquedajugadores(equipos[i],pais)
            break

fundadores = ["Milán","Inter","Juventus"]
