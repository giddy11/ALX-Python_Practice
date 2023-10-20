import random

def roll():
    for i in range(1):
        x = random.randint(1,6)
        y = random.randint(1,6)
        print("({}, {})".format(x, y))