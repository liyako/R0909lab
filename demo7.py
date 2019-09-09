from utility.fib import fib

fib(500)

import utility.fib

utility.fib.fib(1000)

from utility.fib import fib as f

f(10000)

import sys


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()
    pass

if __name__ == '__main__':
    print("inside utility\\fib, name=",__name__)