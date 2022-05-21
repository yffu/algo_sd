# Uses python3
import sys


def get_fibonacci_last_digit_fast(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current % 10


if __name__ == '__main__':
    num = int(input())
    print(get_fibonacci_last_digit_fast(num))
