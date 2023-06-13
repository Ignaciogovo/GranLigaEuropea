# Uso de beatiful soup para sacar datos de la liga
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import conexionsql as cs
# link pagina:
# def EjecucionArbitros():
#     url = "https://todoparaarbitros.com/los-10-mejores-arbitros-de-futbol-de-la-actualidad/"
#     page = requests.get(url) # Optenemos la pagina
#     soup = BeautifulSoup(page.content,'html.parser')
#     # print(soup)
#     prueba = soup.find("div", class_="inside-article")
#     arbitros = prueba.find_all("h4")
#     listaArbitros=[]
#     count = 0
#     # print(prueba)
#     for i in arbitros:
#         if  count == 9:
#             break
#         count +=1
#         listaArbitros.append(i.text) # Cogemos solo el texto de la etiqueta span
#     for i in range(0,9):
#         cs.insertarAbitros(listaArbitros[i])



def configurar_fecha(fecha):
    try:
        fecha_dt = datetime.strptime(fecha, '%d.%m.%Y').date()
    except:
        return fecha  
    fecha_mysql = fecha_dt.strftime('%Y-%m-%d')
    return(fecha_mysql)






def EjecucionArbitros():
    year = (datetime.now()).year
    url = 'https://www.livefutbol.com/arbitro/champions-league-'+str(year-1)+'-'+str(year)+'/'
    page = requests.get(url) # Optenemos la pagina
    soup = BeautifulSoup(page.content,'html.parser')
    # print(soup)
    prueba = soup.find("table", class_="standard_tabelle")
    arbitros_tr = prueba.find_all("tr")
    lista=[]
    for i in range(1,10):
        datos_arbitro=[]
        arbitro_tr = arbitros_tr[i]
        arbitro_tr = list(arbitro_tr)
        # Nombre
        datos_arbitro.append(arbitro_tr[1].text)
        # Año de nacimiento:
        fecha= arbitro_tr[3].text
        datos_arbitro.append(configurar_fecha(fecha))
        # Pais 
        datos_arbitro.append(arbitro_tr[7].text)
        lista.append(datos_arbitro)

    for i in lista:
        cs.insertarAbitros(i)