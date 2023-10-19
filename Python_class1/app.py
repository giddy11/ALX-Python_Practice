
"""
course = '''
Hi Gideon,

Here is our first email to you.

Thank you.

'''

"""

i = 0
while (i < 3):
    guess = int(input("Guess: "))

    if guess != 9 and i != 2:
        i += 1
        continue
    elif (guess == 9):
        print("you got it")
    else:
        print("sorry you failed")


