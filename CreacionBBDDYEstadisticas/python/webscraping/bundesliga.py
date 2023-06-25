from bs4 import BeautifulSoup
import requests
import time
import sofifa
import os
import sys
# Obtén la ruta del directorio padre
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Agrega el directorio padre al sys.path
sys.path.append(parent_dir)
from funciones_globales import unique_list

def EjecucionBundesliga():
    url = "https://www.bundesliga.com/es/bundesliga/clasificacion"
    page = requests.get(url) # Optenemos la pagina
    soup = BeautifulSoup(page.content,'html.parser')
    prueba = soup.find_all("td", class_="team")
    equipos = list()
    count = 0
    pais = "Alemania"
    for i in prueba:
        if count == 18:
            break
        count +=1
        Sininiciales= (i.text)[3:]
        Sininiciales ='' .join(unique_list(Sininiciales.split()))
        equipos.append(Sininiciales) # Cogemos solo el texto de la etiqueta span
    for i in range(0,10):
        if equipos[i] in fundadores:
            continue
        else:
            print("puesto: %d equipo: %s" % (i+1, equipos[i]))
            sofifa.busquedajugadores(equipos[i],pais)
            break

fundadores = ["Bayern","Dortmund"]