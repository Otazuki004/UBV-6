
from HydraUserBot import bot, Hydra

if __name__ == "__main__":
    Hydra.start()
    bot.run()
    with bot:
        bot.send_message("5965055071", "UB Ready")
