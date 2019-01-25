# Uses python3
import sys, math
import numpy as np

def binary_search(a, x):
    """
    param a: list of integers
    param x: number to search for in list a"""
    left, right = 0, len(a)-1

    while right >= left:
        mid = math.floor((left + right)/2)
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid -1
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0] # number of digits in an array
    m = data[n + 1] # number of datapoints to search

    a = data[1 : n + 1] # array to be searched
    x_list = data[n + 2:] # numbers to search for

    # Sample 1
    # a = [1,5,8,12,13]
    # x_list = [8,1,23,1,11]

    # Stress test
    # n = 1000
    # x_list = np.random.randint(low = 0, high = 1000, size = [1,100])[0]
    # a = sorted(np.random.randint(low = 0, high = 1000, size = [1,1000])[0])

    for x in x_list:
        # replace with the call to binary_search when implemented
        # print(linear_search(a, x), end = ' ')
        print(binary_search(a, x), end = ' ')
