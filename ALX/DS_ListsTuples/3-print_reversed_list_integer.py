#!/usr/bin/python3

'''
def print_reversed_list_integer(my_list=[]):
    if my_list:
        mod_list = []
        for m in range(1, len(my_list) + 1):
            mod_list.append(my_list[-m])
        for n in mod_list:
            print("{:d}".format(n))
'''
            


def print_reversed_list_integer(my_list=[]):
    if my_list:
        for integer in reversed(my_list):
            print("{:d}".format(integer))

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)