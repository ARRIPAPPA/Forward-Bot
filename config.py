from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", "23941369"))
    API_HASH = environ.get("API_HASH", "bbd37235e41a95d03bc144ea6bc7b2cd")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6523875009:AAF9AZEmYOiG4u2HuetP3YtGrIjLhudzVoQ") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://ROKU:ROKU@cluster0.nxjre0s.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Fzxforwardbot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5422016608').split()]
    
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
