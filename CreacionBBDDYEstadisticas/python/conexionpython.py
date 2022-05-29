import pymysql
import tweepy
from tweepy import OAuthHandler
def bbddliga():
    db = pymysql.connect(host='xxxxx',user='xxxxx',password='xxxxxx',database='liga',charset='utf8mb4')
    return db



# Si quieres usar un bot de twitter:

def tokensTwitter():
    consumer_key = "xxxxxxxxxxxxxxxx"
    consumer_secret = "xxxxxxxxxxxxxxxxxxxxxx"
    access_token = "xxxxxxxxxxxxxxxxxxxx"
    access_token_secret = "xxxxxxxxxxxxxxxxxxxx"
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth


# (En el caso que se quiera Para hacer conexión con una base de datos en otro servidor)

def replica():
    db = pymysql.connect(host='xxxxxxxxx',user='xxxxxxx',password='xxxxxx',database='liga',charset='utf8mb4') 
    return db

