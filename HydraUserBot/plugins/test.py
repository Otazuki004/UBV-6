from HydraUserBot import Hydra

OWNER_ID = "1985665341"

@Hydra.on_message(filters.command("kick", prefixes=HANDLER) & filters.user(OWNER_ID))

  await client.ban_chat_member(message.chat.id, f"{message.reply_to_message.from_user.id}")

  await client.unban_chat_member(message.chat.id, f"{message.reply_to_message.from_user.id}")
