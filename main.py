"""
In the main file, the class are initialized and the bot
checks the market at regular time interval and buy and sell
stocks in order to make the maximum of money.
"""

import time
from configuration import *
from bot import Bot
import sys

selected_strategy = sys.argv[1]

# time initialisation
t0 = time.strptime(simulation_date, "%Y-%m-%d")
t0 = time.mktime(t0)
i = 0

# box initialisation
bot = Bot(target_companies, time.strftime("%Y-%m-%d", time.gmtime(t0)))


# toutes les timestep secondes
while i < simulation_time:
    t0 += 24 * 3600
    if SHOW_LOG:
        print("Day : ", time.strftime("%Y-%m-%d", time.gmtime(t0)))
    bot.run(time.strftime("%Y-%m-%d", time.gmtime(t0)), selected_strategy)
    time.sleep(timelapse)
    i += 1


bot.stock_state(time.strftime("%Y-%m-%d", time.gmtime(t0)))


print("Bilan de la simulation : ")
print("Montant initial : ", bot.initial_account)
print("Montant final : ", bot.last_account)
