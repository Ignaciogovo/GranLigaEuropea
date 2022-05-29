# Uso de beatiful soup para sacar datos de la liga
from itertools import count
from bs4 import BeautifulSoup
import requests
import conexionsql

# link pagina:
def EjecucionArbitros():
    url = "https://todoparaarbitros.com/los-10-mejores-arbitros-de-futbol-de-la-actualidad/"
    page = requests.get(url) # Optenemos la pagina
    soup = BeautifulSoup(page.content,'html.parser')
    # print(soup)
    prueba = soup.find("div", class_="inside-article")
    arbitros = prueba.find_all("h4")
    listaArbitros=[]
    count = 0
    # print(prueba)
    for i in arbitros:
        if  count == 9:
            break
        count +=1
        listaArbitros.append(i.text) # Cogemos solo el texto de la etiqueta span
    for i in range(0,9):
        conexionsql.insertarAbitros(listaArbitros[i])
