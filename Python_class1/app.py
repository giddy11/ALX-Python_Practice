
"""
course = '''
Hi Gideon,

Here is our first email to you.

Thank you.

'''

"""

'''
guess_count = -1
secret_number = 9
guess_limit = 3

while (guess_count < guess_limit):
    guess = int(input("Guess: "))
    guess_count += 1

    if guess != secret_number and guess_count != 2:
        continue
    elif (guess == 9):
        print("you got it")
        break
    else:
        print("sorry you failed")
        break

'''

running = 1
help_info = '''
start - to start the car
stop - to stop the car
quit - to exit
'''

car_start = 'Car started...Ready to go!'
car_stop = 'Car stopped.'
car_mov = False

while (running):
    user_input = input(">").lower()
    if user_input == 'help':
        print(help_info)
    elif user_input == 'start':
        if(car_mov):
            print("Car is already started!!!")
        else:
            car_mov = True
            print(car_start)
    elif user_input == 'stop':
        if car_mov:
            print(car_stop)
            car_mov = False
        else:
            print("car isn't moving yet!!!")
    elif user_input == 'quit':
        running = 0
    else:
        print("I don't understand that...")
    