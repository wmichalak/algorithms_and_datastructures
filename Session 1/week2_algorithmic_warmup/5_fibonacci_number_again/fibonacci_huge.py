# Uses python3
import sys, math
import numpy as np

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def fast_fibonacci(n):
    n = int(n)
    arr = np.empty(shape=[n+1])

    # Iterate over the integers up to n. Note that range(0,n) is 0:n-1
    for i in range(0,n+1):
        if i<=1:
            arr[i] = i
        else:
            arr[i] = (arr[i-1] + arr[i-2])

    return (arr[n])

def fast_fibonacci_on_mod(n,m):

    arr = np.empty(shape=[n+1])

    # Iterate over the integers up to n. Note that range(0,n) is 0:n-1
    for i in range(0,n+1):
        if i<=1:
            arr[i] = i
        else:
            arr[i] = math.fmod((arr[i-1] + arr[i-2]), m)

    return (arr[n])

def get_fibonacci_huge_faster(n, m):
    """Compute Fn modulo m
     Start by identifying the pisano period (length of repeating sequence)
     :param n: nth fibonacci number
     :param m: divisor in the modulus equation
     :return F(n) mod m

     We can accomplish this task by
     1) calculating the pisano period, p then
     2) identify remainder, r,  from n / p + r then
     3) calculate F(r) mod m

    """

    assert(n >= 1 and n <= 10**18)
    assert(m >= 2 and m <= 10**3)

    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
    # 1) Trick is to create array of remainders and stop when we get 01 repeated
        p = 0
        i = 0
        previous = 0
        for i in range(m**2):
            if i == 1499:
                pause = 1
            current = fast_fibonacci_on_mod(i, m)
            # current = math.fmod(f, m)

            if i>1 and previous == 0 and current == 1:
                p = i - 1 # pisano period
                break
            else:
                previous = current

        if p == 0:
            p = i

        # 2)
        r = math.fmod(n, p)

        # 3) Assume that F(2015) mod 3 = F(7) mod 3 = 1, where 2015 = 251
        return int(math.fmod(fast_fibonacci(r), m))


if __name__ == '__main__':
    ints = input()
    n, m = map(int, ints.split())
    # n, m = 115, 1000
    # print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge_faster(n, m))