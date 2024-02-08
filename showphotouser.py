import requests

chat_id = "6264668799"
urlp = "https://t.me/elhyba"
url = f"https://api.telegram.org/6192207808:AAGCpvOXPoXZaXXmOujHJugdokG9lEOAUQo/getChat?chat_id={chat_id}"

req = requests.get(url).json()
print(req)
