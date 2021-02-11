# pcost.py
#
# Exercise 1.27

with open('Work\Data\portfolio.csv', 'rt') as f:
    next(f)
    total = 0
    for line in f:
        row = line.split(',')
        shares = int(row[1])
        price = float(row[2])
        total += shares * price

print( total)
