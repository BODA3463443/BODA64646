from pyrogram import Client, filters

bot_token = "6192207808:AAGCpvOXPoXZaXXmOujHJugdokG9lEOAUQo"

api_id = 29755247
api_hash = "8dd9fb5fa2782d91b9847ace66eb885a"
app = Client("nb", api_id, api_hash, bot_token=bot_token)


app.start()


@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text(f"Hello")


app.run()

