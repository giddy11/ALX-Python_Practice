#!/usr/bin/python3

if __name__ == "__main__":
    # from calculator_1 import (add, sub, div, mul)
    import calculator_1 as math

    a = 10
    b = 5

    # print(f"{a} + {b} = {add(a, b)}")
    print("{:d} + {:d} = {:d}".format(a, b, math.add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, math.sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, math.mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, math.div(a, b)))