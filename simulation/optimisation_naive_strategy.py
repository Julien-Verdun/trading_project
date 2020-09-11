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
import numpy as np

DEFAULT_STOCKS = ["MSFT", "ADP", "ATOS", "TSLA", "AAPL", "AIR", "OR"]
DEFAULT_SIMULATION_TIME = 40
DEFAULT_TIMELAPSE = 0.005
DEFAULT_SIMULATION_DATE = "2020-01-01"
DEFAULT_STRATEGY = "naive"
# naive strategy parameters
DEFAULT_MOVING_WINDOW = 30
DEFAULT_DECREASE_WINDOW = 3
# commission
DEFAULT_FIXED_COMMISSION = 3
DEFAULT_PROP_COMISSION = 0.02
# inital account amont
DEFAULT_INITIAL_ACCOUNT = 3000


def RunBot(lower, upper):
    # time initialisation
    t0 = date_to_timestamp(args.simulation_date)
    i = 0
    # box initialisation
    bot = Bot(args.stocks, timestamp_to_date(t0), args.simulation_time,
              args.fixed_commission, args.prop_commission, args.moving_window, args.decrease_window, args.log, args.initial_account, lower, upper)

    # every timestep secondes
    while i < args.simulation_time:
        t0 += 24 * 3600
        if args.log:
            print("Day : ", timestamp_to_date(t0))
        bot.run(timestamp_to_date(t0),
                args.strategy, args.log)
        # time.sleep(args.timelapse)
        i += 1

    # if args.log:
    print("\n\nBilan de la simulation : \n", "Lower : ", lower, " - Upper : ", upper,
          "\nMontant initial : ", bot.initial_account, "\nMontant final : ",
          bot.last_account, "\nTotal commissions : ", bot.total_commission,
          "\nTotal transactions : ", bot.total_transaction)
    return bot.last_account, bot.total_commission, bot.total_transaction


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--stocks", type=str, nargs="+",
                        default=DEFAULT_STOCKS)
    parser.add_argument("--simulation_time", type=int,
                        default=DEFAULT_SIMULATION_TIME)
    parser.add_argument("--timelapse", type=float,
                        default=DEFAULT_TIMELAPSE)
    parser.add_argument("--simulation_date", type=str,
                        default=DEFAULT_SIMULATION_DATE)
    parser.add_argument("--strategy", type=str, default=DEFAULT_STRATEGY)
    # naive strategy parameters
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

    range_min = 1
    range_max = 4
    step = 2
    table_test = np.zeros(((step*(range_max-range_min)+1)**2, 5),
                          dtype=int)
    for i in range(step*range_min, step*range_max+1):
        for j in range(step*range_min, step*range_max+1):
            lower = -i/step
            upper = j/step
            last_account, total_commission, total_transaction = RunBot(
                lower, upper)
            table_test[(i-step*range_min)*(step*(range_max-range_min)+1)+j-step*range_min, :] = [-i, j,
                                                                                                 int(last_account), int(total_commission), int(total_transaction)]

    print(table_test)

    index_max = np.argmax(table_test, axis=0)[2]

    print("Better coefficient : ",
          table_test[index_max][0]/step, table_test[index_max][1]/step, table_test[index_max][2])

    text_table_test = "lower*" + str(step) + " upper*" + str(
        step) + " last_account total_commission total_transaction"
    for line in table_test.tolist():
        text_table_test += " ".join([str(elt) for elt in line])
        text_table_test += "\n"
    with open("optimisation_results.txt", "w") as optimisation_results:
        optimisation_results.write(text_table_test)


if __name__ == '__main__':
    main()
else:
    pass
