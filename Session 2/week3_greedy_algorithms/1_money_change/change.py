# Uses python3

def get_change(m):
    """ Find minimum number of coins
    :param m: total money to give change
    :return: number of coins (i.e. length of coins list) for a set of coins in {1, 5, 10} that does
    not exceed value m
    """
    change = (10, 5 ,1) # Already sorted to start with largest amount

    # Greedy algorithm will sample with largest value until it is filled and then go to next
    coins = []  # list of coins used
    # total value
    value = 0  # total value
    for c in change:
        while value <= m:
            if value + c > m:
                break
            coins += [c]
            value += c

    return len(coins)

if __name__ == '__main__':
    # input total amount of integer money
    # return minimum number of coins with denominations 1,5,10 that changes money
    m = int(input())
    assert (m >= 1 and m <= 10**3)
    print(get_change(m))
