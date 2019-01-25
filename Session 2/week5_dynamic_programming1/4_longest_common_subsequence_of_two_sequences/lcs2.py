#Uses python3

import sys
import numpy as np

def lcs2(s, t):

    # Allocate array
    d = np.empty([len(s)+1, len(t)+1])

    # Build array, starting with edges known
    for i in np.arange(0, len(s)+1):
        d[i, 0] = 0
    for j in np.arange(0, len(t)+1):
        d[0, j] = 0

    for i in np.arange(1, len(s)+1):
        for j in np.arange(1, len(t)+1):
            if s[i-1] == t[j-1]:
                d[i, j] = d[i-1, j-1] + 1
            else:
                d[i, j] = max(d[i, j - 1],
                              d[i-1, j])


    return int(max(np.max(d[:, len(t)]), np.max(d[len(s), :])))

    # LISa, preva = ls(a)
    # LISb, prevb = ls(b)
    #
    # for i, vala in enumerate(LISa):
    #     for i, valb in enumerate(LISb):


def get_sequence(A, LIS, prev, i):
    # Get the longest sequence from
    j = len(LIS) - 1
    sequence = [A[i]]
    while j > 0:
        sequence.append(A[prev[j]])
        j = prev[j]

    return min(len(a), len(b))

def ls(A):
    LIS = [1] * len(A)
    prev = [-1] * len(A)

    # Generate tables for LIS number and previous index for LIS
    for i in range(len(A)):
        for j in range(i):
            if A[j] < A[i] and LIS[i] < LIS[j] + 1:
                LIS[i] = LIS[j] + 1
                prev[i] = j

    return LIS, prev

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    # Tests
    # a = [2,7,8,3]
    # b = [5,2,8,7]

    print(lcs2(a, b))
