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
    print(prueba)
    for i in prueba:
        if count == 20:
            break
        count +=1
        equipos.append(i.text) # Cogemos solo el texto de la etiqueta span
    for i in range(0,20):
        print("puesto: %d equipo: %s" % (i+1, equipos[i]))
        # sofifa.busquedajugadores(equipos[i])


EjecucionBundesliga()