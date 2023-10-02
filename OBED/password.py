#!/usr/bin/python3

username = "giddy11"
password = "gidoski@1"

user_username = input("Enter your username: ").lower()
user_password = input("Enter your password: ")

if (user_username == username and user_password == password):
    print("Successfully logged in")
elif (user_username == username):
    print("Wrong password")
else:
    print("Username doesnt exist!!")