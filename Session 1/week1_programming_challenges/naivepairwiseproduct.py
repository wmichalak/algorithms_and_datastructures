# Uses python3
import numpy as np

# n = int(input())
# a = [int(x) for x in input().split()]

def pairwise(a,n):
    sorted_a = a.sort()
    return a[-1]*a[-2]

def slowpairwise(a,n):
    product = 0
    for i in range(n):
       for j in range(i + 1, n):
           product = max(product, a[i] * a[j])
    return product

if __name__ == '__main__':

    # Generate random sets
    for i in range(100):
        # Get random number for a in uniform distribution
        n = int(np.random.rand(1)*100) + 1
        a = (np.random.random_sample((n,)) * 100 ).astype(int)
        # print('a:{}, n:{}'.format(a,n))
        f = pairwise(a,n)
        fslow = slowpairwise(a,n)

        if f == fslow:
            print('OK')
        elif f!= fslow:
            print('{} != {}'.format(f,fslow))