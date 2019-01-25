# Uses python3
import numpy as np
import time
# import sys

# Rercursive approach
# def calc_fib(n):
#     if (n <= 1):
#         return n
#
#     return calc_fib(n - 1) + calc_fib(n - 2)
#
# n = int(input())
# print(calc_fib(n))

# Efficient approach
# For a given fibonacci number, calculate series, store in memory and

def fast_fibonacci(n):

    arr = np.empty(shape=[n+1])

    # Iterate over the integers up to n. Note that range(0,n) is 0:n-1
    for i in range(0,n+1):
        if i<=1:
            arr[i] = i
        else:
            arr[i] = arr[i-1] + arr[i-2]

    return (int(arr[n]))

if __name__ == '__main__':
    # n = sys.stdin.read()
    n = int(input())
    print(fast_fibonacci(n))

