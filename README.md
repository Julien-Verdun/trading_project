# Trading bot

Creation of a trading bot.

## Team

- Baptiste Desarnauts
- Maxime Peter
- Julien Verdun

#

## Stocks API

For this project we use **yfinance** API of Python.

In a command prompt, in either **simulation** or **production** folder, run the command line :

```
python main_simulation.py
```

or

```
python main_production.py
```

following by the parameters below :

- `--stocks` _arg_ : arg is one or more stock's names (for example "MSFT ADP ATOS")
- `--timelapse` _arg_ : arg is the time, in second, that the bot is waiting between every day of the simulation
- `--simulation_time` _arg_ : arg is the total simulation duration in days
- `--simulation_date` _arg_ : arg is the date of the first day of the simulation (for example "2020-01-01")
- `--strategy` _arg_ : arg is the name of the choosen strategy (naive, classic, ml)
- `--lower` _arg_ : arg is the lower bound parameter of the naive strategy
- `--upper` _arg_ : arg is the upper bound parameter of the naive strategy
- `--moving_window` _arg_ : arg is the size (in days) of the moving window parameter of the naive strategy
- `--decrease_window` _arg_ : arg is the size (in days) of the decrease window parameter of the naive strategy
- `--log` : used to display more informations about the simulation
- `--fixed_commission` _arg_ : arg is the amount, in euros, of the fixed commission, applied to every transaction
- `--prop_commission` _arg_ : arg is the rate, of the proportinnal commission applied to every transaction
- `--bot_file` _arg_ : arg is the name of the file which includes bot parameters
- `--stock_file` _arg_ : arg is the name of the file which includes stock parameters
- `--wallet_file` _arg_ : arg is the name of the file which includes wallet parameters
- `--initial_account` _arg_ : arg is the initial amount available in the wallet

For example, if you run the command line

```
python main_simulation.py --log --strategy naive --lower -3 upper 6
```

you will run the simulation, with every logs and the naive strategy with parameters -3 and 6.

with strategy the strategy name :

- classic :
- naive

#

## Bot operation

The bot is working as follow :

- every day, the bot calls the strategy (different strategies implemented, see the description below)
- the strategy observes the stock market for a short period of time and decides whether or not the bot should buy, sell, or do nothing with every stocks
- the bot uses the strategy predictions to buy and sell stocks
- the wallet is updated for every bot actions, the available cash and stock amount are updated by taking into account the commission fees
- at the end, it is possible to see how much money did the bt win or lose at the stock market, hoping that it wins more money than it loses.

### Naive strategy

This strategy is very naive. It takes the stock's variations during a time period (for example 30 days) and computes the mean variation, i-e the sum of price evolution from day to day, divided by the length of the time period. The mean variation shows if the stock did gloabally increased or decreased during the period.

Then, the strategy predicts what to do next with the stock :

- buy the stock if the mean variation is higher than a given value (for example 2%)
- sell the stock if the mean variation is lower than a given value
- do nothing if the mean variation is close to 0.

Basically, this strategy buys stocks that are increasing.

The **lower** and **upper** boundaries are optimised by testing the different possibilities and choosing the combination with the better result (maximal final money amount).

### The commission fees

When one buys a stock or sells it, it exists many costs, fees, brokerage fee and commissions, debited by the bank and the stock market.

In a first time, we decided to model all those fees, simply with 2 components :

- a fixed commission sets to 3€
- a proportionnal commission sets to 2% of the stock value

and those fees are debited every single time a stock is bought or sold. The choosen values are overestimated to make sure in a real simulation we won't lose money.

## Simulation

We decided to implement first a bot able to simulate several days or months of the stocks market very quickly. The limiting factor in our project is the API time request. In fact, our strategies compute the prediction very quickly, but to get the result from a request to the API, it almost takes few seconds.
To simulate quickly the result of our strategies on a year of stock market's data, we decided to get the data from the API only once, at the initilisation of the class.

## Production

Explain \_\_\_\_ production
