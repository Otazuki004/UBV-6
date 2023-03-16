from config import LOG_GROUP_ID
from HydraUserBot import bot, Hydra

if __name__ == "__main__":
    Hydra.start()
    bot.run()
    with bot:
        bot.send_message(f"{LOG_GROUP_ID}", "Nyaa Hydra Ready Boi!")
