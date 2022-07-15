import os

from telethon import Button, events

from JE313P import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/2ad68bd0e391a69163d0a.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@BK_ZT"
)

CAPTION = f"**سرعة البينج:** {ms}\n المالك:『{ALIVE}』"


@JE313P.on(events.NewMessage(pattern="^/البينج"))
async def _(event):
    UMM = [[Button.url("السورس", "https://t.me/CR_T2")]]
    await JE313P.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
