 from pyrogram import Client
 api_id = 9026412
 api_hash = "b54245b1cad1cc35963ff925d93e53af"

with Client("account", api_id, api_hash) as app:
    app.send_message("me", "Greeting from **Pyrogram**!")

 