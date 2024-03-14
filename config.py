from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", "23941369"))
    API_HASH = environ.get("API_HASH", "bbd37235e41a95d03bc144ea6bc7b2cd")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7047021941:AAE972UWujL-Wr1UOcek_VsvVnw9QDl5xm4") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://Forward:Forward@cluster0.2kpl6qb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Fzxforwardbot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5422016608 6748415360').split()]
    
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
