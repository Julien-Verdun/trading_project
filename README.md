# Trading bot

Creation of a trading bot.

## Team

- Baptiste Desarnauts
- Maxime Peter
- Julien Verdun

#

## Stocks API

For this project we use **yfinance** API of Python.

In a command prompt, run the command :

########################## Mettre ici
les choses a mettre dans la ligne de commande ##############

```
python main.py [strategy]
```

with strategy the strategy name :

- classic
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

### The commission fees

When one buys a stock or sells it, it exists many costs, fees, brokerage fee and commissions, debited by the bank and the stock market.

In a first time, we decided to model all those fees, simply with 2 components :

- a fixed commission sets to 3€
- a proportionnal commission sets to 2% of the stock value

and those fees are debited every single time a stock is bought or sold. The choosen values are overestimated to make sure in a real simulation we won't lose money.
