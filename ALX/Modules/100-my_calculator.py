#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1

num_of_args = len(sys.argv) - 1

if num_of_args != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

a, op, b = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])

if (op == '+'):
    result = calculator_1.add(a, b)
elif (op == '-'):
    result = calculator_1.sub(a, b)
elif (op == '*'):
    result = calculator_1.mul(a, b)
elif (op == '/'):
    result = calculator_1.div(a, b)
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

print("{} {} {} = {}" .format(a, op, b, result))
exit(0)