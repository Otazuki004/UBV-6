from HydraUserBot import Hydra as bot
from pyrogram import filters

@bot.on_message(filters.command("unban") & filters.user(1985665341)) 
def ban(bot, message):
	bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
	bot.send_message(message.chat.id, f"Successfully Unbaned! {message.reply_to_message.from_user.mention}.")
