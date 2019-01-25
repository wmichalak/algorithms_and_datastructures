# Uses python3
import sys
import itertools
import numpy as np

def brute_force_partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        # print(c)
        sums = [None] * 3
        for i in range(3):
            # print([A[k] for k in range(len(A)) if c[k] == i])
            # print(sum(A[k] for k in range(len(A)) if c[k] == i))
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0

def partition2(A):
    sum_A = sum(A)

    if sum_A % 2 != 0:
        return 0
    sum_2 = sum_A // 2

    z = np.ones(shape=[sum_2 + 1, len(A) + 1]) * float('-Inf')

    for j in range(len(A) + 1):
        z[0,j] = 1

    for i in range(1, sum_2 + 1):
        z[i,0] = 0

    for j in range(1,len(A) + 1):
        for i in range(0, sum_2 + 1):
            if z[i, j-1]:
                z[i, j] = 1
                if i + A[j-1] <= sum_2:
                    z[i + A[j-1], j] = 1
            elif z[i, j] != 1:
                z[i, j] = 0

    return z[i, j]

def partition3(A):
    sum_A = sum(A)

    if sum_A % 3 != 0:
        return 0
    sum_3 = sum_A // 2

    z = np.ones(shape=[sum_3 + 1, len(A) + 1]) * float('-Inf')

    for j in range(len(A) + 1):
        z[0,j] = 1

    for i in range(1, sum_3 + 1):
        z[i,0] = 0

    for j in range(1,len(A) + 1):
        for i in range(0, sum_3 + 1):
            if z[i, j-1]:
                z[i, j] = 1
                if i + A[j-1] <= sum_3:
                    z[i + A[j-1], j] = 1
            elif z[i, j] != 1:
                z[i, j] = 0

    return z[i, j]

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    # n = 4
    # A = [3,3,3,3]
    # n = 12
    # A = [1,2,3,4,5,5,7,7,8,10,12,19,25]
    # n = 5
    # A = [1,2,3,4,5,5,7,7,8,10,12,19,25]
    print(brute_force_partition3(A))
    # print(partition2(A))
