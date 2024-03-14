from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", "16501053"))
    API_HASH = environ.get("API_HASH", "d8c9b01c863dabacc484c2c06cdd0f6e")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6556754160:AAHbrDQ3e9qQmZ5oVOdwb0ZvN2qiXHbJqNM") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://Forward:Forward@cluster0.2kpl6qb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5422016608 6748415360').split()]
    
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
