from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("• ᴄᴏᴍᴍᴀɴᴅs •", data="help_back")
    ],
    [
        Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/DevanshXBots"),
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/DevanshXBotChats")
    ],
    [
        Button.url("• sᴏᴜʀᴄᴇ •", "https://github.com/Devansh-Bots/SpamX")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"➥ **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [𝐃ᴇᴠᴀɴsʜ](https://t.me/DamnDevansh)**\n\n"
        TEXT += f"➥ **DᴇᴠXSᴘᴀᴍ ᴠᴇʀsɪᴏɴ :** `M3.3`\n"
        TEXT += f"➥ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `3.11.3`\n"
        TEXT += f"➥ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                    event.chat_id,
                    "https://te.legra.ph/file/525009db27a57d4159e91.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
                )
