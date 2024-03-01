# Decorators

"""
    Decorators:
        Decorators in Python are a powerful feature that allows you to modify 
        or extend the behavior of functions or methods without changing their 
        actual code. Decorators are implemented using functions that take another 
        function as an argument and return a new function that typically extends or 
        modifies the behavior of the original function.
"""

from functools import wraps

translations = {
    "rosemilk_buy" :{
        "ta": "enaku rosemilk vangithara mudiuma",
        "en": "Can you buy me a Rosemilk",
        "sp": "atrtete atete"
    }
}

def dec(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg, lang = target_function(*args, **kwargs)
        return translations[msg][lang] + " 🥤"
    return wrapper

@dec
def say(lang = "en"):
    msg = "rosemilk_buy"
    return msg,lang

print(say())

"""
    Output:
        Can you buy me a Rosemilk 🥤
"""