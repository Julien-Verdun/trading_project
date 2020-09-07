# Trading bot

Creation of a trading bot.

## Team

- Baptiste Desarnauts
- Maxime Peter
- Julien Verdun

## Stocks API

For this project we use **yfinance** API of Python.

In a command prompt, run the command :

```
python main.py [strategy]
```

with strategy the strategy name :

- classic
- naive

### Naive strategy

This strategy is very naive. It takes the stock's variations during a time period (for example 30 days) and computes the mean variation, i-e the sum of price evolution from day to day, divided by the length of the time period. The mean variation shows if the stock did gloabally increased or decreased during the period.

Then, the strategy predicts what to do next with the stock :

- buy the stock if the mean variation is higher than a given value (for example 2%)
- sell the stock if the mean variation is lower than a given value
- do nothing if the mean variation is close to 0.

Basically, this strategy buys stocks that are increasing.
