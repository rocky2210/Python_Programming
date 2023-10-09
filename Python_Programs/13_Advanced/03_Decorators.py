
from functools import wraps

translations = {
    "rosemilk_buy" :{
        "ta": "enaku rosemilk vangithara mudiuma",
        "en": "Can you buy me a Rosemilk",
        "sp": "atrtete atete"
    }
}

def beg(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg, lang = target_function(*args, **kwargs)
        return translations[msg][lang] + " 🥤"
    return wrapper

@beg
def say(lang = "en"):
    msg = "rosemilk_buy"
    return msg,lang

print(say())