import conexionpython as cp
import conexionsql as cs
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
    local = cs.selectNombreClub(local)
    visitante = cs.selectNombreClub(visitante)
    api = tweepy.API(auth)
    texto = local+" "+str(gol_local )+" VS "+visitante+" "+str(gol_visitante)
    api.update_status(texto)

def twittearFinal():
    auth=cp.tokensTwitter()
    campeon = cs.selectCampeonLiga()
    temporada = str(cs.selectTemporada())
    api = tweepy.API(auth)
    texto =  "¡¡FINAAAL DE LA TEMPORADA: "+ temporada + "!! Felicidades a " + campeon +" por su campeonato ligero."
    api.update_status(texto)