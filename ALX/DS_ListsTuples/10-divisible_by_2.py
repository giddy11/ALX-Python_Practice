#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new = []
    for m in my_list:
        a = m % 2 == 0
        if a:
            new.append(True)
        else:
            new.append(False)
    return new


my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)
leng = len(list_result) - 1

# i = 0
# while i < len(list_result):
#     print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
#     i += 1

for le in range(leng):
    print("{:d} {:s} divisible by 2".format(my_list[le], "is" if list_result[le] else "is not"))