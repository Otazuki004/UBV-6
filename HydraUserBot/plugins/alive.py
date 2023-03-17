import time

from pyrogram import __version__ as pyrover
from pyrogram import filters

from config import ALIVE_TEXT, HANDLER, Hydra1, OWNER_ID
from HydraUserBot import StartTime, get_readable_time, Hydra


@Hydra.on_message(filters.command("alive", prefixes=HANDLER) & filters.user(OWNER_ID))
def alive(_, m):
    you = Hydra.get_me()
    start_time = time.time()
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 3)
    uptime = get_readable_time((time.time() - StartTime))
    m.reply_photo(
        Hydra1, caption=ALIVE_TEXT.format(you.mention, pyrover, ping_time, uptime)
    )
