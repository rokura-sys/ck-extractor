from telethon.tl.functions.users import GetFullUserRequest
from start import ADMIN_GROUP

async def starts(event):
    user = await event.client(GetFullUserRequest(event.sender_id))
    await event.reply(
        f"a nice stream splitter bot. but it can only be used from [Group](tg://user?id={ADMIN_GROUP})"
    )
