"""
In the main file, the class are initialized and the bot
checks the market at regular time interval and buy and sell
stocks in order to make the maximum of money.
"""

import time
from src.components.bot import Bot
import argparse
from src.utils.time_utils import *
from src.utils.json_utils import *
import sys


DEFAULT_STOCKS = ["MSFT", "ADP", "ATOS", "TSLA", "AAPL", "AIR", "OR"]
DEFAULT_INITIAL_QUANTITY = 1
DEFAULT_SIMULATION_TIME = 40
DEFAULT_TIMELAPSE = 0.1
DEFAULT_SIMULATION_DATE = "2020-01-01"
DEFAULT_STRATEGY = "naive"
# naive strategy parameters
DEFAULT_LOWER = -2
DEFAULT_UPPER = 5
DEFAULT_MOVING_WINDOW = 30
DEFAULT_DECREASE_WINDOW = 3
# commission
DEFAULT_FIXED_COMMISSION = 3
DEFAULT_PROP_COMISSION = 0.02
# inital account amont
DEFAULT_INITIAL_ACCOUNT = 3000


def RunBot():
    # time initialisation
    t0 = date_to_timestamp(args.simulation_date)
    i = 0
    print("Hi")
    # box initialisation
    bot = Bot(args.stocks, timestamp_to_date(t0), args.initial_quantity, args.simulation_time,
              args.fixed_commission, args.prop_commission, args.moving_window, args.decrease_window, args.log, args.initial_account, args.lower, args.upper)

    # every timestep secondes
    while i < args.simulation_time:
        t0 += 24 * 3600
        if args.log:
            print("Day : ", timestamp_to_date(t0))
        bot.run(timestamp_to_date(t0),
                args.strategy, args.log)
        time.sleep(args.timelapse)
        # bot.store_state(timestamp_to_date(t0))
        i += 1

    bot.stock_state(timestamp_to_date(t0))

    # if args.log:
    print("Bilan de la simulation : ")
    print("Montant initial : ", bot.initial_account)
    print("Montant final : ", bot.last_account)
    print("Total commissions : ", bot.total_commission)
    print("Total transactions : ", bot.total_transaction)


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--stocks", type=str, nargs="+",
                        default=DEFAULT_STOCKS)
    parser.add_argument("--initial_quantity", type=int,
                        default=DEFAULT_INITIAL_QUANTITY)
    parser.add_argument("--simulation_time", type=int,
                        default=DEFAULT_SIMULATION_TIME)
    parser.add_argument("--timelapse", type=float,
                        default=DEFAULT_TIMELAPSE)
    parser.add_argument("--simulation_date", type=str,
                        default=DEFAULT_SIMULATION_DATE)
    parser.add_argument("--strategy", type=str, default=DEFAULT_STRATEGY)
    # naive strategy parameters
    parser.add_argument("--lower", type=int, default=DEFAULT_LOWER)
    parser.add_argument("--upper", type=int, default=DEFAULT_UPPER)
    parser.add_argument("--moving_window", type=float,
                        default=DEFAULT_MOVING_WINDOW)
    parser.add_argument("--decrease_window", type=float,
                        default=DEFAULT_DECREASE_WINDOW)

    parser.add_argument("--log", action='store_true', default=False)

    parser.add_argument("--fixed_commission", type=float,
                        default=DEFAULT_FIXED_COMMISSION)
    parser.add_argument("--prop_commission", type=float,
                        default=DEFAULT_PROP_COMISSION)
    parser.add_argument("--initial_account", type=float,
                        default=DEFAULT_INITIAL_ACCOUNT)

    global args

    args = parser.parse_args()

    RunBot()


if __name__ == '__main__':
    main()
else:
    pass
