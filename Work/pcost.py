# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        next(f)
        total = 0
        for line in f:
            row = line.split(',')
            shares = int(row[1])
            price = float(row[2])
            total += shares * price

    return total

print("Total portfolio: ksh. ", portfolio_cost('Work\Data\portfolio.csv'))