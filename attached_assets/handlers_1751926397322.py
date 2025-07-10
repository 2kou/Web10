from telethon import TelegramClient, events
from config.settings import API_ID, API_HASH, BOT_TOKEN, ADMIN_ID
import logging
from bot.license import check_license
from bot.payment import process_payment

client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
logging.basicConfig(level=logging.INFO)

@client.on(events.NewMessage(pattern="/start"))
async def start(event):
    await event.respond("Bienvenue sur TeleFeed !\nTapez /valide pour activer vos accès premium si vous avez une licence.")

@client.on(events.NewMessage(pattern="/valide"))
async def valide(event):
    await check_license(event, client)

@client.on(events.NewMessage(pattern="/payer"))
async def payer(event):
    await process_payment(event, client)

def start_bot():
    print("Bot lancé !")
    client.run_until_disconnected()
