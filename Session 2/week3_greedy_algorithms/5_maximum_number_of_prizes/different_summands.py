# Uses python3
import sys, time

def optimal_summands(n):

    if n == 1 or n == 2:
        return [n]

    # Start with 1 and work up. I can't see a way to arbitrarily pick a first prize
    p = [1] # number of prizes
    sum_p = 1
    while sum_p < n:
        if (sum_p + (p[-1] + 1)) <= n: # add +1 to last
            next_prize = p[-1] + 1
            p += [next_prize]
            sum_p += next_prize
        else: # fix last entry to equal total
            sum_p -= p[-1]
            p[-1] = n - sum_p
            sum_p += p[-1]

    return p

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
