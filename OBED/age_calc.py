#!/usr/bin/python3

yob = input("What's your year of birth: ")
mob = input("Month of birth (0 - 12): ")
dob = input("Day of the month: ")
current_year = input("In which year are you now? ")
age = int(current_year) - int(yob)

print("Your date of birth is ", end="")
print(dob,mob,yob, sep="-")

print("Your age is: ",age)
