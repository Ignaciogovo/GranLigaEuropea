from webbrowser import get
from selenium import webdriver
from selenium.webdriver.support.ui import Select # Permite seleccionar valores dentro de una lista desplegable.
from selenium.webdriver.chrome.options import Options #Permite opciones a la hora de hacer la ejecucion.
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests
from datetime import date
import sys    
    
get_url = "https://sofifa.com/team/481/sevilla-fc/"

page = requests.get(get_url) # Optenemos la pagina
soup = BeautifulSoup(page.content,'html.parser')
others = soup.find("div", class_="bp3-card player")
estadio = others.find("li", class_="ellipsis")
estadio = (estadio.text).replace("Home Stadium", "")
print(estadio)