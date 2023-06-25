# Importacion de sofifa
import sofifa as sf
#Importacion de ligas:
import Premier
import santander
import bundesliga
import serieA
import ligue1


import Busqueda_besoccer as besoccer
from arbitros import EjecucionArbitros
from time import sleep
import sys
import os
from datetime import datetime

# in the sys.path list
sys.path.append('.\\')  
# Obtén la ruta del directorio padre
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Agrega el directorio padre al sys.path
sys.path.append(parent_dir)



import conexionsql as cs








#Premier:
def inglaterra(year):
    pais = "Inglaterra"
    url_clasificacion="https://www.besoccer.com/competition/table/premier_league/"
    fundadores = ["Man. City","Liverpool","Chelsea","Arsenal","Tottenham Hotspur","Man. Utd"]
        # Inserción CLUBS fundadores:

        #Tottemham
    url_ = "https://sofifa.com/team/18/tottenham-hotspur/"
    nombre = "Tottenham Hotspur"
    sf.IngresoDatos(url_,nombre,pais)

        #Chelsea
    url_ = "https://sofifa.com/team/5/chelsea/"
    nombre = "Chelsea"
    sf.IngresoDatos(url_,nombre,pais)

        #Liverpool
    url_ = "https://sofifa.com/team/9/liverpool/"
    nombre = "Liverpool"
    sf.IngresoDatos(url_,nombre,pais)

        #Manchester united
    url_ = "https://sofifa.com/team/11/manchester-united/"
    nombre = "Manchester United"
    sf.IngresoDatos(url_,nombre,pais)

        #Arsenal
    url_ = "https://sofifa.com/team/1/arsenal/"
    nombre = "Arsenal"
    sf.IngresoDatos(url_,nombre,pais)

        #Manchester City
    url_ = "https://sofifa.com/team/10/manchester-city/"
    nombre = "Manchester City"
    sf.IngresoDatos(url_,nombre,pais)

    # Mejor clasificado:
    # Premier.EjecucionPremier(year)
    besoccer.Busqueda_clasificacion(year,url_clasificacion,fundadores,pais)


# Santander
def españa(year):
    pais = "España"
    url_clasificacion = "https://www.besoccer.com/competition/table/primera_division/"
    fundadores = ["Real Madrid","Barcelona","Atlético"]
        # Inserción CLUBS fundadores:

        #Barcelona
    url_ = "https://sofifa.com/team/241/fc-barcelona/"
    nombre = "Barcelona"
    sf.IngresoDatos(url_,nombre,pais)

        #Real Madrid
    url_ = "https://sofifa.com/team/243/real-madrid-cf/"
    nombre = "Real Madrid"
    sf.IngresoDatos(url_,nombre,pais)

        #Atlético de Madrid
    url_ = "https://sofifa.com/team/240/atletico-de-madrid/"
    nombre = "Atlético de Madrid"
    sf.IngresoDatos(url_,nombre,pais)

        # Mejor clasificado:
    # santander.EjecucionSantander(year)
    besoccer.Busqueda_clasificacion(year,url_clasificacion,fundadores,pais)



# SERIE A
def italia(year):
    pais = "Italia"
    url_clasificacion = "https://www.besoccer.com/competition/table/serie_a/"
    fundadores = ["Milan","Inter","Juventus"]

        # Inserción CLUBS fundadores:

        #juventus
    url_ = "https://sofifa.com/team/45/juventus/"
    nombre = "Juventus"
    sf.IngresoDatos(url_,nombre,pais)

        #Inter de Milán
    url_ = "https://sofifa.com/team/44/inter/"
    nombre = "Inter de Milán"
    sf.IngresoDatos(url_,nombre,pais)

        #AC Milán
    url_ = "https://sofifa.com/team/47/ac-milan/"
    nombre = "AC Milán"
    sf.IngresoDatos(url_,nombre,pais)

        # Mejor clasificado:
    # serieA.EjecucionSerieA(year)
    besoccer.Busqueda_clasificacion(year,url_clasificacion,fundadores,pais)



# Bundesliga:
def alemania(year):
    pais = "Alemania"
    url_clasificacion="https://www.besoccer.com/competition/table/bundesliga/"
    fundadores = ["Bayern München","B. Dortmund"]
    # Inserción CLUBS fundadores:

        #Borussia Dortmund
    url_ = "https://sofifa.com/team/22/borussia-dortmund/"
    nombre = "Borussia Dortmund"
    sf.IngresoDatos(url_,nombre,pais)

        #Bayern de Múnich
    url_ = "https://sofifa.com/team/21/fc-bayern-munchen/"
    nombre = "Bayern de Múnich"
    sf.IngresoDatos(url_,nombre,pais)

        # Mejor clasificado:
    # bundesliga.EjecucionBundesliga(year)
    besoccer.Busqueda_clasificacion(year,url_clasificacion,fundadores,pais)

# Ligue1
def francia(year):
    pais = "Francia"
    url_clasificacion="https://www.besoccer.com/competition/table/ligue_1/"
    fundador = "PSG"

    # Inserción CLUBS fundadores:

        #PSG
    url_ = "https://sofifa.com/team/73/paris-saint-germain/"
    nombre = "Paris saint-germain"
    sf.IngresoDatos(url_,nombre,pais)

    # Mejor clasificado:
    # ligue1.EjecucionLigue1(year)
    besoccer.Busqueda_clasificacion(year,url_clasificacion,fundador,pais)




# Captura el tiempo de inicio
inicio = datetime.now()
# Sacamos el año
year = (datetime.now()).year


cs.historico_jugadores()
inglaterra(year)
sleep(1)
españa(year)
sleep(1)
italia(year)
sleep(1)
alemania(year)
sleep(1)
francia(year)
sleep(1)
EjecucionArbitros(year)
cs.insertarTemporada()
cs.insertarClasificacion()


fin = datetime.now()

tiempo_total = fin - inicio
print("Tiempo total:", tiempo_total.total_seconds(), "segundos")





# 12:21 minutos