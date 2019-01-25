#Uses python3

import sys
import numpy as np
import time

def lcs3(a, b, c):
    # Allocate array
    d = np.zeros([len(a) + 1, len(b) + 1, len(c) + 1])


    for i in np.arange(1, len(a) + 1):
        for j in np.arange(1, len(b) + 1):
            for k in np.arange(1, len(c) + 1):
                if i == 0 or j == 0 or k == 0:
                    d[i, j, k] = 0

                if(a[i - 1] == b[j - 1] == c[k - 1]):
                    d[i, j, k] = d[i - 1, j - 1, k - 1] + 1
                else:
                    d[i, j] = max(d[i - 1, j, k],
                                  d[i, j - 1, k],
                                  d[i, j, k - 1])
                                  # d[i, j - 1, k - 1],
                                  # d[i - 1, j, k - 1],
                                  # d[i - 1, j - 1, k])

    max_lcs = int(d[i, j, k])
    return max_lcs

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]

    # Test 1
    # a = [1,2,3]
    # b = [2,1,3]
    # c = [1,3,5]
    # #
    # # Test 2
    # a = [8,3,2,1,7]
    # b = [8,2,1,3,8,10,7]
    # c = [6,8,3,1,4,7]

    # t0 = time.time()
    max_lcs = lcs3(a, b, c)
    print(max_lcs)
    # print(time.time() - t0)
