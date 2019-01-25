# Uses python3
import sys, time
import numpy as np

def get_change(money):
    coins = (1, 3, 4)
    min_num_coins = (money+1) * [float('Inf')]
    min_num_coins[0] = 0
    # Fill table of all values up to value of money
    for m in range(1, money+1):
        for coin in coins:
            if m >= coin: # only test on values that are larger than the coins available
                num_coins = min_num_coins[m - coin] + 1
                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins

    return min_num_coins[money]



if __name__ == '__main__':
    m = int(sys.stdin.read())
    # m = 34
    # t0 = time.time()
    print(get_change(m))

    # Stress test
    # for randint in np.random.randint(0, 1000, size=100):
    #     t0 = time.time()
    #     print(randint, get_change(randint),time.time() - t0)
