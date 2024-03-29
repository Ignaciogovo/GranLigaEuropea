import pymysql
import tweepy
from tweepy import OAuthHandler
import os
from dotenv import load_dotenv
# Obtiene la ruta absoluta del directorio actual
dir_path = os.path.dirname(os.path.abspath(__file__))

# Concatena el nombre del archivo .env al final de la ruta
env_path = os.path.join(dir_path, '.env')

# Carga las variables de entorno desde el archivo .env
load_dotenv(env_path)

# Carga las variables de entorno desde el archivo .env
# Obtén la contraseña desde la variable de entorno
password = os.getenv('PASSWORD_DB')
ip = os.getenv('IP_DB')
usuario = os.getenv('USER_DB')
database = os.getenv('DATABASE_DB')
consumer_key=os.getenv('CONSUMER_KEY')
consumer_secret=os.getenv('CONSUMER_SECRET')
access_token=os.getenv('ACCESS_TOKEN')
access_token_secret=os.getenv('ACCESS_TOKEN_SECRET')
# Utiliza la contraseña en tu código
def bbddliga():
    db = pymysql.connect(host=ip,user=usuario,password=password,database=database,charset='utf8mb4')
    return db




# Si quieres usar un bot de twitter:

def tokensTwitter():
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth


# (En el caso que se quiera Para hacer conexión con una base de datos en otro servidor)

def replica():
    db = pymysql.connect(host='xxxxxxxxx',user='xxxxxxx',password='xxxxxx',database='liga',charset='utf8mb4') 
    return db

