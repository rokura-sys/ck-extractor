import re ,os

from telethon import TelegramClient, events
if __name__ == '__main__':
    from helpers import eventreciever

APP_ID = int(os.environ.get("APP_ID", 12345))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN_GROUP = int(os.environ.get("ADMIN_GROUP", 12345))

@client.on(events.NewMessage(pattern="/start"))
async def _(event):
    await eventreciever.start(event)


@client.on(events.NewMessage(pattern="/help"))
async def _(event):
    await eventreciever.helps(event)

@client.on(events.NewMessage(pattern="/split_everything"))
async def _(event):
    await eventreciever.split(event)

@client.on(events.callbackquery.CallbackQuery(data=re.compile("<<")))
async def _(event):
    await eventreciever.start(event)


@client.on(events.callbackquery.CallbackQuery(data=re.compile("status")))
async def _(event):
    await eventreciever.status(event)

if __name__ == '__main__':
    try:
        client = TelegramClient("bot", APP_ID, API_HASH).start(bot_token=BOT_TOKEN)
    except Exception:
        exit()
    client.run_until_disconnected()
