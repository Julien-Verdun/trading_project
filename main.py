"""
In the main file, the class are initialized and the bot 
checks the market at regular time interval and buy and sell 
stocks in order to make the maximum of money.
"""

import time
from configuration import *
# from bot import Bot


#bot = Bot(target_companies)

# initialisation du temps

#t0 = datetime.timestamp(datetime(2015, 1, 1)) + 24 * 3600 * 1000

t0 = time.strptime("01-01-2010", "%d-%m-%Y")
t0 = time.mktime(t0)
i = 0
# toutes les timestep secondes
while i < simulation_time:
    t0 += 24 * 3600
    print("go : ", time.gmtime(t0))

    time.sleep(timelapse)
    i += 1


# partir d'une date fixe, la passer en argument du bot etc, et incrementer le jour
