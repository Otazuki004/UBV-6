from HydraUserBot import Hydra as bot
from pyrogram import filters

@bot.on_message(filters.command("ban") & filters.user(1985665341)) 
def ban(bot, message):
	reply = m.reply_to_message
_reply = ""
if not reply:
	bot.send_message(message.chat.id, "Please Reply Someone To Ban")
if reply.from_user:
	bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
     bot.send_message(message.chat.id, f"Successfully Banned! {message.reply_to_message.from_user.mention}.")
)