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


DEFAULT_STOCKS = ["MSFT", "ADP", "ATOS", "TSLA", "AAPL", "AIR", "OR"]
DEFAULT_INITIAL_QUANTITY = 1
DEFAULT_TIMELAPSE = 1 * 3600
# strategy
DEFAULT_STRATEGY = "naive"
# naive strategy parameters
DEFAULT_LOWER = -2
DEFAULT_UPPER = 2
DEFAULT_MOVING_WINDOW = 30
DEFAULT_DECREASE_WINDOW = 3
# commission fees
DEFAULT_FIXED_COMMISSION = 3
DEFAULT_PROP_COMISSION = 0.02
# state storage files
DEFAULT_BOT_FILE = "./src/data/bot.JSON"
DEFAULT_STOCK_FILE = "./src/data/stock.JSON"
DEFAULT_WALLET_FILE = "./src/data/wallet.JSON"
# inital account amont
DEFAULT_INITIAL_ACCOUNT = 3000


def RunBot():
    # time initialisation
    t0 = time.time()
    """
    Initialisation du bot avec un JSON ?
    lui donner en argument les fichier stock et wallet pour les initialiser la ou on les a laissé
    """

    # box initialisation
    bot = Bot(args.stocks, timestamp_to_date(t0), args.initial_quantity,
              args.fixed_commission, args.prop_commission, args.moving_window,
              args.decrease_window, args.log, args.initial_account, args.lower, args.upper,
              args.stock_file, args.wallet_file, args.bot_file)

    bot.load_state(timestamp_to_date(t0))

    if bot.check_not_already_ran(timestamp_to_date(t0)):
        bot.run(timestamp_to_date(t0),
                args.strategy, args.log)
        if args.log:
            print("RUN : ", timestamp_to_date(t0))

        bot.store_state(timestamp_to_date(t0))
        bot.stock_state(timestamp_to_date(t0))

        print("Day assessment : ")
        print("Initial amount : ", bot.initial_account)
        print("Final amount : ", bot.last_account)
        print("Total commissions : ", bot.total_commission)
        print("Total transactions : ", bot.total_transaction)
    else:
        print("Day already ran")


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--stocks", type=str, nargs="+",
                        default=DEFAULT_STOCKS)
    parser.add_argument("--initial_quantity", type=int,
                        default=DEFAULT_INITIAL_QUANTITY)
    parser.add_argument("--timelapse", type=float,
                        default=DEFAULT_TIMELAPSE)
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

    parser.add_argument("--bot_file", type=str,
                        default=DEFAULT_BOT_FILE)
    parser.add_argument("--stock_file", type=str,
                        default=DEFAULT_STOCK_FILE)
    parser.add_argument("--wallet_file", type=str,
                        default=DEFAULT_WALLET_FILE)
    parser.add_argument("--initial_account", type=float,
                        default=DEFAULT_INITIAL_ACCOUNT)

    global args

    args = parser.parse_args()

    RunBot()


if __name__ == '__main__':
    main()
else:
    pass
