"""
In the main file, the class are initialized and the bot
checks the market at regular time interval and buy and sell
stocks in order to make the maximum of money.
"""

import time
from bot import Bot
<<<<<<< HEAD
import argparse 
=======
import sys
>>>>>>> 98e83226ed3c9015bbec6a5bfc5253117fd5e571

selected_strategy = sys.argv[1]

DEFAULT_STOCKS = ["MSFT", "ADP", "ATOS", "TSLA", "AAPL", "AIR", "OR"]
DEFAULT_SIMULATION_TIME = 40
DEFAULT_TIMELAPSE = 0.1
DEFAULT_SIMULATION_DATE = "2020-01-01"
DEFAULT_STRATEGY = "naive"
DEFAULT_LOWER = -2
DEFAULT_UPPER = 2
DEFAULT_MOVING_WINDOW = 30




def RunBot():
    # time initialisation
    t0 = time.strptime(args.simulation_date, "%Y-%m-%d")
    t0 = time.mktime(t0)
    i = 0

    # box initialisation
    bot = Bot(args.stocks, time.strftime("%Y-%m-%d", time.gmtime(t0)), args.simulation_time)


    # toutes les timestep secondes
    while i < args.simulation_time:
        t0 += 24 * 3600
        if args.log:
            print("Day : ", time.strftime("%Y-%m-%d", time.gmtime(t0)))
        bot.run(time.strftime("%Y-%m-%d", time.gmtime(t0)), args.strategy, args.log)
        time.sleep(args.timelapse)
        i += 1


    bot.stock_state(time.strftime("%Y-%m-%d", time.gmtime(t0)))

    if args.log:
        print("Bilan de la simulation : ")
        print("Montant initial : ", bot.initial_account)
        print("Montant final : ", bot.last_account)




def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--stocks", type=str, nargs="+", default=DEFAULT_STOCKS)
    parser.add_argument("--simulation_time", type=int, default=DEFAULT_SIMULATION_TIME)
    parser.add_argument("--timelapse", type=float, default=DEFAULT_TIMELAPSE)
    parser.add_argument("--simulation_date", type=str, default=DEFAULT_SIMULATION_DATE)
    parser.add_argument("--strategy", type=str, default=DEFAULT_STRATEGY)
    parser.add_argument("--lower", type=int, default=DEFAULT_LOWER)
    parser.add_argument("--upper", type=int, default=DEFAULT_UPPER)
    parser.add_argument("--moving_window", type=float, default=DEFAULT_MOVING_WINDOW)
    parser.add_argument("--log", action='store_true', default=False)

    global args

    args = parser.parse_args()

    RunBot()


if __name__ == '__main__':
    main()
else:
    pass