# Uses python3
import sys, math
import numpy as np

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fibonacci_sum_faster(n):

    arr = np.empty(shape=[n+1])

    # Iterate over the integers up to n. Note that range(0,n) is 0:n-1
    for i in range(0,n+1):
        if i<=1:
            arr[i] = i
        else:
            arr[i] = (arr[i-1] + arr[i-2]) % 10

    return int(arr.sum() % 10)

if __name__ == '__main__':
    n = int(input())
    # n=1000903
    assert(n >= 0 and n <= 10**18)
    # print(fibonacci_sum_naive(n))
    print(fibonacci_sum_faster(n))
