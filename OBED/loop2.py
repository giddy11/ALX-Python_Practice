#!/usr/bin/python3

counter = 1

while (counter <= 6):
    if (counter == 2):
        print(counter)
    elif (counter == 3):
        counter += 1
        continue
    elif (counter == 5):
        pass
    else:
        print(counter)

    counter += 1

print("End!!")