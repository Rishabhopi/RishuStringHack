# TEAM RISHU ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "14050586"
    API_HASH = "42a60d9c657b106370c79bb0a8ac560c"  
    TOKEN = os.environ.get("TOKEN", "YOUR BOT TOKEN")
    MONGO_URL = "mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority"
    START_PIC = "https://envs.sh/OTc.jpg"
    SUDOERS = filters.user(["5186826758"])
