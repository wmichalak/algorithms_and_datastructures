# Uses python3
import sys
import random, time
import numpy as np

def partition3(a, l, r):
    """
    Move pointer l to the right and pointer r to the left. At each stage, ask whether the
    :param a: list of ints
    :param l: left index
    :param r: right index
    :return: split index, j and a
    """

    k = random.randint(l, r)

    a[l], a[k] = a[k], a[l]
    x = a[l]
    for i in range(l + 1, r + 1):
        if a[i] > x:
            for j in range(r,l,-1):
                if j == i:
                    a[l], a[i-1] = a[i-1], a[l]
                    return i-1, a
                if a[j] < x:
                    a[i], a[j] = a[j], a[i]
                    r = j
                    break

    a[i], a[l] = a[l], a[i]
    return i, a

def randomized_quick_sort3(a, l, r):
    if l >= r:
        return a
    m, a = partition3(a, l, r)
    a = randomized_quick_sort3(a, l, m - 1)
    a = randomized_quick_sort3(a, m + 1, r)

    return a

def partition2(a, l, r):
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
        # print(a)
    a[l], a[j] = a[j], a[l]
    return j

def randomized_quick_sort2(a, l, r):
    if l >= r:
        return
    m = partition2(a, l, r)
    randomized_quick_sort2(a, l, m - 1)
    randomized_quick_sort2(a, m + 1, r)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    a = randomized_quick_sort3(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

    # Testing
    # n = 1000
    # a = np.random.randint(low = 0, high = 1000, size = [1,n])[0]
    # a[np.random.randint(low = 0, high = 1000, size = [1,200])[0]] = 100
    # # a = [3, 1, 7, 6, 9, 5, 10, 2, 4, 8]
    # t0 = time.time()
    # a = randomized_quick_sort3(a, 0, n - 1)
    # print(time.time() - t0)
    # for x in a:
    #     print(x, end=' ')

    #Compare to slower?
    # t0 = time.time()
    # a = randomized_quick_sort2(a, 0, n - 1)
    # print(time.time() - t0)
    # for x in a:
    #     print(x, end=' ')
