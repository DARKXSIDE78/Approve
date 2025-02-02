from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "17417255"))
    API_HASH = getenv("API_HASH", "73d424d9847f968130cd5b41946f7a5d")
    BOT_TOKEN = getenv("BOT_TOKEN", "7600707476:AAFxxEjFUp74OfKH8LCfsjuhkvwTYMGnCbM")
    FSUB = getenv("FSUB", "@GenAnimeOfc")
    CHID = int(getenv("CHID", "-1002187486464"))
    SUDO = list(map(int, getenv("SUDO", "6302971969 7086472788").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://nitinkumardhundhara:DARKXSIDE78@cluster0.wdive.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
