from pyrogram import filters

from Felicia.services.pyrogram import pbot as Felicia


@Felicia.on_message(filters.command("webshot", ["."]))
async def webshot(clien, message):
    try:
        user = message.command[1]
        await message.delete()
        link = f"https://webshot.deam.io/{user}/?delay=2000"
        await client.send_document(message.chat.id, link, caption=f"{user}")
    except:
        await message.delete()
        await client.send_message(message.chat.id, "**Wrong Url**")
