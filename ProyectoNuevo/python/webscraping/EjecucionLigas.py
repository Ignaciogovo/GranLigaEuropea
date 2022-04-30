# Importacion de sofifa
import sofifa as sf
#Importacion de ligas:
import Premier
import santander
import bundesliga
import serieA
import ligue1
from arbitros import EjecucionArbitros
from time import sleep
#Premier:
def inglaterra():
    pais = "Inglaterra"
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
    Premier.EjecucionPremier()


# Santander
def españa():
    pais = "España"
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
    santander.EjecucionSantander()



# SERIE A
def italia():
    pais = "Italia"

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
    serieA.EjecucionSerieA()



# Bundesliga:
def alemania():
    pais = "Alemania"

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
    bundesliga.EjecucionBundesliga()

# Ligue1
def francia():
    pais = "Francia"

    # Inserción CLUBS fundadores:

        #PSG
    url_ = "https://sofifa.com/team/73/paris-saint-germain/"
    nombre = "Paris saint-germain"
    sf.IngresoDatos(url_,nombre,pais)

    # Mejor clasificado:
    ligue1.EjecucionLigue1()






inglaterra()
sleep(1)
españa()
sleep(1)
italia()
sleep(1)
alemania()
sleep(1)
francia()
sleep(1)
EjecucionArbitros()