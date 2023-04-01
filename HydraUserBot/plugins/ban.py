from HydraUserBot import Hydra as bot
from pyrogram import filters

@bot.on_message(filters.command("ban") & filters.user(1985665341)) 
def ban(_, m):
    reply = m.reply_to_message
    _reply = ""
    if not reply:
        bot.send_message(m.chat.id, "Please Reply Someone To Ban")
        if reply.from_user:
            bot.ban_chat_member(m.chat.id, message.reply_to_message.from_user.id)
            bot.send_message(m.chat.id, f"Successfully Banned! {message.reply_to_message.from_user.mention}."),
