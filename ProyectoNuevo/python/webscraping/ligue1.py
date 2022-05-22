from bs4 import BeautifulSoup
import requests
import time
import sofifa
# link pagina:
def EjecucionLigue1():
    url = "https://www.ligue1.com/ranking"
    page = requests.get(url) # Optenemos la pagina
    soup = BeautifulSoup(page.content,'html.parser')
    prueba = soup.find_all("span", class_="GeneralStats-clubName desktop-item")
    equipos = list()
    count = 0
    pais = "Francia"
    for i in prueba:
        if count == 20:
            break
        count +=1
        equipos.append(i.text) # Cogemos solo el texto de la etiqueta span
    for i in range(0,3):
        if equipos[i] == fundador:
            continue
        else:
            print("puesto: %d equipo: %s" % (i+1, equipos[i]))
            equipo = (equipos[i]).title()
            sofifa.busquedajugadores(equipo,pais)

            break

fundador = "PARIS SAINT-GERMAIN"
EjecucionLigue1()
