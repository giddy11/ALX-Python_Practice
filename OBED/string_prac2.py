#!/usr/bin/python3

fname = input("Firstname: ")
lname = input("Lastname: ")
age = int(input("Age: "))

# using old style formatting
# print("Your name is %s %s and age is %d" %(fname, lname, age))

# using new style formatting
# print("Your name is {} {} and age is {}".format(fname, lname, age)) 

# using new style formatting
# print("Your name is {:s} {:s} and age is {:d}".format(fname, lname, age))

# using new style formatting
# print("Your name is {1} {0} and age is {2}".format(fname, lname, age)) 

# using new style formatting
# print("Your name is {f} {l} and age is {a}".format(f = fname, l = lname, a = age))

# using new style formatting
# print(f"Your name is {fname} {lname} and age is {age}")

# using new style formatting
# print(f"Your name is {fname:s} {lname:s} and age is {age:d}") 

print(f"Your name is {fname} {lname} and age is {age} and {96}") 