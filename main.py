"""
In the main file, the class are initialized and the bot 
checks the market at regular time interval and buy and sell 
stocks in order to make the maximum of money.
"""

import time
from datetime import *
from configuration import *
from Bot import Bot


bot = Bot(target_companies)

# initialisation du temps
t0 = datetime.timestamp('2019-01-01') + 24 * 3600 * 1000

i = 0
# toutes les timestep secondes
while i < 4:
    t0 += 24 * 3600 * 1000
    print("t0", t0)

    print("go : ", time.strftime("%Y-%m-%d", time.gmtime()))

    time.sleep(5)
    i += 1


# partir d'une date fixe, la passer en argument du bot etc, et incrementer le jour
