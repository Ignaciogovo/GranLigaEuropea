import sys
sys.path.append('ProyectoLiga')
import conexionpython as cp
from conexionsql import selectNombreClub 
import tweepy
def twittearJornada(jornada):
    auth=cp.tokensTwitter()
    api = tweepy.API(auth)
    # Publicar tweet
    texto = "Inicio de la Jornada: "+str(jornada)
    if jornada==1:
        texto = "Comienza la temporada con el inicio de la jornada: "+str(jornada)
    api.update_status(texto)

def twittearPartido(local,visitante,gol_local,gol_visitante):
    auth=cp.tokensTwitter()
    local = selectNombreClub(local)
    visitante = selectNombreClub(visitante)
    api = tweepy.API(auth)
    texto = local+" VS "+visitante+" Resultado: "+str(gol_local )+"-"+str(gol_visitante)
    api.update_status(texto)


