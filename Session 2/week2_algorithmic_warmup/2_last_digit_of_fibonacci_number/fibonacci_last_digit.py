# Uses python3
import sys
import numpy as np
import math

# def get_fibonacci_last_digit_naive(n):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current  = 1
#
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#
#     return current % 10

def get_fibonacci_last_digit_last(n):
    """Store the last digit and calculate the sum % 10. can't store full number because of memory constraints"""
    arr = np.empty(shape=[n+1])

    for i in range(0, n+1):
        if i<=1:
            arr[i] = i
        else:
            # Store the last digit by finding the remainder using mod
            arr[i] = math.fmod(arr[i-1] + arr[i-2],10)

    return int(arr[n])

if __name__ == '__main__':
    # Examples
    # print(get_fibonacci_last_digit_last(3))
    # print(get_fibonacci_last_digit_last(331))
    # print(get_fibonacci_last_digit_last(327305))

    n = int(input())
    print(get_fibonacci_last_digit_last(n))



