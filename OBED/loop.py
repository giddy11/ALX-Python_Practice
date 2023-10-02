#!/usr/bin/python3

name = input("Name: ")

# for charac in range(5):
#     print(charac)


for charac in name:
    if (charac == "d"):
        print(charac)
        continue

else:
    print("Not found")