import conexionpython as cp
import conexionsql as cs
import tweepy
import os
from dotenv import load_dotenv
# Obtiene la ruta absoluta del directorio actual
dir_path = os.path.dirname(os.path.abspath(__file__))

# Concatena el nombre del archivo .env al final de la ruta
env_path = os.path.join(dir_path, '.env')

# Carga las variables de entorno desde el archivo .env
load_dotenv(env_path)
control_twitter=os.getenv('CONTROL_TWITTER')

def twittearJornada(jornada):
    # Comprobamos si se quiere twitterar
    if control_twitter == 'S':
        try:
            auth=cp.tokensTwitter()
            api = tweepy.API(auth)
            # Publicar tweet
            texto = "Inicio de la Jornada: "+str(jornada)
            if jornada==1:
                texto = "Comienza la temporada con el inicio de la jornada: "+str(jornada)
            api.update_status(texto)
        except:
            print("Error al realizar el tweet inicio jornada")
def twittearPartido(local,visitante,gol_local,gol_visitante):
    # Comprobamos si se quiere twitterar
    if control_twitter == 'S':
        try:
            auth=cp.tokensTwitter()
            local = cs.selectNombreClub(local)
            visitante = cs.selectNombreClub(visitante)
            api = tweepy.API(auth)
            texto = local+" "+str(gol_local )+" VS "+visitante+" "+str(gol_visitante)
            api.update_status(texto)
        except:
            print("Error al realizar el tweet partido: "+str(local)+" "+str(gol_local )+" VS "+str(visitante)+" "+str(gol_visitante))
def twittearFinal():
    # Comprobamos si se quiere twitterar
    if control_twitter == 'S':
        try:
            auth=cp.tokensTwitter()
            campeon = cs.selectCampeonLiga()
            temporada = str(cs.selectTemporada())
            api = tweepy.API(auth)
            texto =  "¡¡FINAAAL DE LA TEMPORADA: "+ temporada + "!! Felicidades a " + campeon +" por su campeonato ligero."
            api.update_status(texto)
        except:
            print("Error al realizar tweet final temporada")

def twittearPaginaweb(jornada):
    # Comprobamos si se quiere twitterar
    if control_twitter == 'S':
        try:
            auth=cp.tokensTwitter()
            api = tweepy.API(auth)
            # Publicar tweet
            texto = "Ya estan disponibles todos los datos de la jornada "+str(jornada)+" en http://granligaeuropea.freetzi.com/"
            api.update_status(texto)
        except:
            print("Error al realizar tweet final jornada")





def twittearMensaje(mensaje):
    # Comprobamos si se quiere twitterar
    if control_twitter == 'S':
        try:
            auth=cp.tokensTwitter()
            api = tweepy.API(auth)
            api.update_status(mensaje)
        except:
            print("error al realizar insert mensaje")
