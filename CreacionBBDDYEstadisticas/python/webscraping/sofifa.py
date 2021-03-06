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
# in the sys.path list
sys.path.append('.\\')        
import conexionsql
#Esta función busca a los jugadores a partir del nombre del equipo.
def busquedajugadores(nombre_equipo,pais):
    website = 'https://sofifa.com/teams'
    path = 'C:\driversChrome\chromedriver.exe'
    opciones = Options()
    opciones.add_argument("--headless") # Permite hacer el script en segundo plano.
    driver = webdriver.Chrome(chrome_options=opciones, executable_path=path)
    driver.get(website)
    #Aceptamos las cookies (No hace falta, solo era para cuando estaba visible)
    # Cookiess = driver.find_element(By.CLASS_NAME,'banner_continueBtn--3KNKl')
    # Cookiess.click()
    # time.sleep(2)
    # Cookiess2 = driver.find_element(By.CLASS_NAME,'button_button--lgX0P.details_save--1ja7w')
    # Cookiess2.click()

    #Buscamos al equipo
    busquedaEquipo = driver.find_element(By.NAME,'keyword')
    busquedaEquipo.send_keys(nombre_equipo)
    busquedaEquipo.send_keys(Keys.ENTER)
    time.sleep(2)
    #Sacamos la url actual para usar beatiful soup
    url_equipos = driver.current_url
    # Usamos beatiful soup
    page = requests.get(url_equipos) # Optenemos la pagina
    soup = BeautifulSoup(page.content,'html.parser')
    # Si no sale ningun equipo en la lista se ejecuta este if:
    if soup.find("td", class_="col-name-wide") == None:
        nombre_equipo2 = nombre_equipo[:4] #Acortamos el nombre del equipo para reducir errores en la diferencia de escritura
        # Volvemos a Buscar el equipo
        busquedaEquipo = driver.find_element(By.NAME,'keyword')
        busquedaEquipo.send_keys(nombre_equipo2)
        busquedaEquipo.send_keys(Keys.ENTER)
        time.sleep(2)
        # volvemos a sacar la url actual:
        url_equipos = driver.current_url
        page = requests.get(url_equipos) # Optenemos la pagina
        soup = BeautifulSoup(page.content,'html.parser')

    listaEquipos = soup.find("td", class_="col-name-wide")
    urlPrimerequipo = listaEquipos.find("a") #Buscamos el primer enlace de la lista de equipos:
    link = urlPrimerequipo.get('href') #Sacamos el link interno de la pagina
    #Eliminamos espacios al principio y al final
    equipoNombre=nombre_equipo.strip()
    IngresoDatos("https://sofifa.com"+link,equipoNombre,pais)
    





def IngresoDatos(get_url,equipoNombre,pais):
    id_estadio = sacarEstadio(get_url)
    # Ingresamos el club 
    conexionsql.insertarclub(equipoNombre,pais,id_estadio)
    # time.sleep(1)
    # Obtenemos el id de ese club:
    id_equipo = conexionsql.SelectClub(equipoNombre)
    # Usamos la url para obtener los datos de los jugadores de cada club
    page = requests.get(get_url) # Optenemos la pagina
    soup = BeautifulSoup(page.content,'html.parser')
    lista = soup.find("tbody", class_="list")
    for a in lista.find_all("a"):
        if a.find("div", class_="ellipsis") == None: #Si un hijo del enlace no tiene una clase ellipsis se continua el for
            continue
        else:
            link = a.get('href') #Sacamos el link interno de la pagina del jugador
            # Sacamos e insertamos datos jugadores
            sacardatosJugadores("https://sofifa.com"+link,id_equipo)
    # Actualizados datos del equipo
    conexionsql.updateclub(id_equipo)

def sacardatosJugadores(get_url,id_equipo):
    page = requests.get(get_url) # Optenemos la pagina
    soup = BeautifulSoup(page.content,'html.parser')
    datos = soup.find("div", class_="info")
    #Buscamos el nombre:
    nombre = datos.find("h1").text
    #Buscamos el pais:
    pais = datos.find("a")
    pais = pais.get("title")
    #Sacamos Posicion,fecha,cm y kg a partir de funciones creadas:
    datosindi=datos.find("div")
    posicion = diferenciarPosicion(datosindi.text)
    fecha=diferenciarfecha(datosindi.text)
    cm = diferenciarCm(datosindi.text)
    kg = diferenciarKg(datosindi.text)
    #Buscamos el valor de mercado:
    sacarvalor= soup.find("section", class_="card spacing")
    #Buscamos el valor economico entre las otras estadisticas:
    for i in sacarvalor.find_all("div", class_="block-quarter"):
        if i.find("div", class_="sub").text == "Value": #Si el texto del div es igual a value:
            valor = i.find("div").text
            valor=valor.replace("Value","").replace("€","") #Eliminamos los datos no numericos del valor
    valor=convertirValor(valor)
    Ldatos=(nombre,id_equipo,posicion,int(kg),int(cm),pais,int(valor),fecha,id_equipo,posicion,int(kg),int(cm),pais,int(valor)) # Duplicamos datos para usar on duplicate key update
    conexionsql.insertarjugador(Ldatos)

#Funciones para sacar datos individuales de la cadena de texto:

def diferenciarPosicion(cadena):
    sinespacios = cadena.lstrip()#Elimina los espacios de la izquierda
    posicion=sinespacios[:3] #Sacamos los tres primeros caracteres de la cadena de texto
    posicion = posicion.replace(" ", "")#Elimina los espacios
    posicion=str(convertirPosiciones(posicion))
    return posicion

def diferenciarfecha(cadena):
    parentesis1 = cadena.find("(")
    parentesis2 = cadena.find(")")
    fecha = cadena[parentesis1+1:parentesis2]
    fecha = convertirFechas(fecha)
    return str(fecha)

def diferenciarCm(cadena):
    cadena = cadena.replace(" ", "")
    cm=cadena.find("cm")
    parentesis = cadena.find(")")
    return cadena[parentesis+1:cm]

def diferenciarKg(cadena):
    cadena = cadena.replace(" ", "")
    cm=cadena.find("cm")
    kg = cadena.find("kg")
    return cadena[cm+2:kg]


# Conversiones de los datos para que sean más leibles
    # Convertimos las fechas para que sea legible en sql
def convertirFechas (cadena):
    sinespacios = cadena.replace(" ", "")
        #Sacamos el dia
    coma = cadena.find(",")
    dia = int(sinespacios[3:coma].replace(",", ""))
    #Sacamos mes
    cadenames=sinespacios[:3]
    months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
    for month in months:
        if cadenames ==month:
            mes = int((months.index(month)+1))
    #sacamos año
    año = int(sinespacios[coma:].replace(",", ""))
    #Convertimos los datos en una fecha
    new_date = date(año,mes,dia)
    return new_date

    #Convertimos el valor en miles o millones
def convertirValor (cadena):
    sinespacios = cadena.replace(" ", "")
    numerocaracteres = len(sinespacios)
    if sinespacios[numerocaracteres-1] == "M":
        valor = sinespacios.replace("M","")
        valor = float(valor)
        valor = valor * 1000000
    else:
        valor = sinespacios.replace("K","")
        valor = float(valor)
        valor = valor * 1000
    valor = int(valor)
    return(valor)

def convertirPosiciones (cadena):
    sinespacios = cadena.replace(" ", "")
    for key in posiciones: #Iteramos las posiciones
        valores = posiciones.get(key)
        valores = tuple(valores) # Volvemos a convertir cada valor de las posiciones en tuplas
        for k in valores:
            if sinespacios == k: # Comparamos la cadena con las posiciones más especificas en las tuplas
                return(key)



# Sacamos el sacarEstadio
def sacarEstadio(get_url):
    page = requests.get(get_url) # Optenemos la pagina
    soup = BeautifulSoup(page.content,'html.parser')
    others = soup.find("div", class_="bp3-card player")
    estadio = others.find("li", class_="ellipsis")
    estadio = (estadio.text).replace("Home Stadium", "")
    conexionsql.insertarEstadios(estadio)
    id_estadio=conexionsql.SelectEstadio(estadio)
    return(id_estadio)


#Datos de las posiciones
portero= ("GK","0")
defensa =("RB","RB","CB","LB","LWB","RWB")
centrocampista=("RM","CD","CM","LM","CAM","LAM","RAM","CDM","RDM","LDM")
delantero = ("RW","ST","CF","LW","LS","RS","LF","RF")
posiciones={
    "Portero" : portero,
    "Defensa" : defensa,
    "Centrocampista" : centrocampista,
    "Delantero" : delantero
}
