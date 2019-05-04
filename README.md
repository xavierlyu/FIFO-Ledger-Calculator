# FIFO Ledger Calculator

This python calculator will aggregate all the transactions in a given ledger. It will print out the total holdings of all assets in the portfolio, the total current value of the portfolio and the total realized profit and loss of the portfolio by asset. It uses first-in-first-out (FIFO) algorithm to compute realized profit. 

The ledger of transactions in the form of a comma-separated file has the following columns

```
DATE,ASSET,PRICE,AMOUNT
```

Transaction represent inflows and outflows of a portfolio of assets, where DATE represents the date of a transaction (YYYY/MM/DD), ASSET is a string of 3 to 6 letters identifying the asset bought or sold, PRICE is the dollar price of the asset and the AMOUNT is (positive or negative) amount of the asset that was bought or sold.

```
transactions1.csv:

DATE,ASSET,PRICE,AMOUNT
02/03/2018,ETH,600,20
02/07/2018,ETH,615,-10
```

Running: 

`$ fifo.py transactions1.csv`

Produces output transactions1.out: 

```
Portfolio (1 asset)
ETH: 10 $6150
Total portfolio value: $6150
Portfolio P&L (1 asset): 
ETH: $150
Total P&L: $150
```
