# bounce.py
#
# Exercise 1.5

height = 100
for bounce in range(10):
    bounceHeight = round(height*3/5, 4)
    height= bounceHeight
    print (bounceHeight)
