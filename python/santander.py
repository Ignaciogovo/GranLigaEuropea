from bs4 import BeautifulSoup
import requests
import time
import sofifa
# link pagina:
url = "https://www.laliga.com/laliga-santander/clasificacion"
page = requests.get(url) # Optenemos la pagina
soup = BeautifulSoup(page.content,'html.parser')
prueba = soup.find_all("div", class_="styled__ShieldContainer-lo8ov8-0 bkblFd shield-desktop")
equipos = list()
count = 0
for i in prueba:
    if count == 20:
        break
    count +=1
    equipos.append(i.text) # Cogemos solo el texto de la etiqueta span
for i in range(0,3):
    print("puesto: %d equipo: %s" % (i+1, equipos[i]))
    sofifa.busquedajugadores(equipos[i])