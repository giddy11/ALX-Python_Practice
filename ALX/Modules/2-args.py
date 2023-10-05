#!/usr/bin/python3

import sys


if __name__ == "__main__":
    num_of_args = len(sys.argv) - 1

'''
    if num_of_args == 0:
        print("0 arguments.")
    elif num_of_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_of_args))
'''

plural_suffix = "s" if num_of_args != 1 else ":"
print("{} argument{}".format(num_of_args, plural_suffix))

for i, arg in enumerate(sys.argv[1:], start=1):
    print("{}: {}".format(i, arg))


# sys.stderr.write('This is stderr\n')
# sys.stderr.flush()
# sys.stdout.write('This is stdout\n')

# print(sys.argv)

# if len(sys.argv) > 1:
#     print(float(sys.argv[1])+5)

# def main(arg):
#     print(arg)

# main(sys.argv[1])