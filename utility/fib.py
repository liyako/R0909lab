import sys


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()
    pass
if __name__ == '__main__':
    fib(int(sys.argv[1]))