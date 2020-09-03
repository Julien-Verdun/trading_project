"""
In the main file, the class are initialized and the bot
checks the market at regular time interval and buy and sell
stocks in order to make the maximum of money.
"""

import time
from configuration import *
#from bot import Bot


# time initialisation
t0 = time.strptime(simulation_date, "%d-%m-%Y")
t0 = time.mktime(t0)
i = 0

# box initialisation
# bot = Bot(target_companies,)


# toutes les timestep secondes
while i < simulation_time:
    t0 += 24 * 3600
    print("go : ", time.strftime("%d-%m-%Y", time.gmtime(t0)))
    # bot.run(strftime("%d-%m-%Y", time.gmtime(t0))
    time.sleep(timelapse)
    i += 1
