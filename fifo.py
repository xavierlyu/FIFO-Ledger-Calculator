import csv
import sys
from collections import deque

"""
To run this program, type `python3 fifo.py [path/to/file]`
Precondition: 
    inputted file is in .csv format
    dates are in order
    price and amount are integers
    prices are nonnegative

Postcondition:
    losses will be displayed as $-## instead of -$##
    order of assets is in the order they are first read from the file
    if an asset has 0 shares after trading, it will still be displayed
    no new line after the last line
"""

file = sys.argv[1]
output_file = open(file[:-4] + ".out", "w")

# a dict containing current price, amount and profit of each asset
data = {}
# a list of queue. Keeps track of the oldest shares bought of each asset
q = {}


def calc_profit(asset, amount, sold_price):
    """
    Return the profit (or loss) gained when an asset is sold
    """
    if len(q) == 0 or len(q[asset]) == 0:
        output_file.write("Error: can't sell more than what you have")
        output_file.close()
        sys.exit(0)
    else:
        oldest_bought = q[asset].popleft()
        if amount > oldest_bought["amount"]:
            return (
                (sold_price - oldest_bought["price"]) * oldest_bought["amount"]
            ) + calc_profit(asset, amount - oldest_bought["amount"], sold_price)
        elif amount == oldest_bought["amount"]:
            return (sold_price - oldest_bought["price"]) * oldest_bought["amount"]
        else:
            q[asset].appendleft(
                {
                    "price": oldest_bought["price"],
                    "amount": oldest_bought["amount"] - amount,
                }
            )
            return (sold_price - oldest_bought["price"]) * amount


with open(file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    is_first_line = True
    for row in csv_reader:
        if is_first_line:
            is_first_line = False
        else:
            date = row[0]
            asset = row[1]
            price = row[2]
            amount = row[3]

            if asset in data:
                temp = data[asset]

                if int(amount) < 0 and abs(int(amount)) > temp["amount"]:
                    output_file.write("Error: can't sell more than what you have")
                    output_file.close()
                    sys.exit(0)

                profit = 0
                if int(amount) < 0:  # if selling
                    profit = calc_profit(asset, abs(int(amount)), int(price))
                else:  # if buying
                    q[asset].append({"price": int(price), "amount": int(amount)})

                data[asset] = {
                    "price": int(price),
                    "amount": temp["amount"] + int(amount),
                    "profit": temp["profit"] + profit,
                }
            else:
                if int(amount) < 0:
                    output_file.write(
                        "Error: detected sale before purchase (short selling is not supported)"
                    )
                    output_file.close()
                    sys.exit(0)

                data[asset] = {"price": int(price), "amount": int(amount), "profit": 0}
                q[asset] = deque()
                q[asset].append({"price": int(price), "amount": int(amount)})

    if len(data) > 1:
        output_file.write(f"Portfolio ({len(data)} assets)\n")
    else:
        output_file.write(f"Portfolio ({len(data)} asset)\n")

    totalValue = 0
    for k, v in data.items():
        value = v["price"] * v["amount"]
        totalValue += value
        output_file.write(f'{k}: {v["amount"]} ${value}\n')

    output_file.write(f"Total portfolio value: ${totalValue}\n")

    if len(data) > 1:
        output_file.write(f"Portfolio P&L ({len(data)} assets): \n")
    else:
        output_file.write(f"Portfolio P&L ({len(data)} asset): \n")

    totalPL = 0
    for k, v in data.items():
        profit = v["profit"]
        totalPL += profit
        output_file.write(f"{k}: ${profit}\n")

    output_file.write(f"Total P&L: ${totalPL}")
    output_file.close()
    sys.exit(0)
