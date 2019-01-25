# Uses python3
import sys

def greedy_calculator(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def dp_calculator(n):
    previous = [0, 0]
    min_calcs = (n+1) * [float('Inf')]
    # min number of calcs to reach given value corresponding to index

    # initialize
    min_calcs[0] = 0
    min_calcs[1] =  0
    for i in range(2,n+1):
        ops_at_i = []
        prev_at_i = []
        if i % 3 == 0:
            ops_at_i.append(min_calcs[i // 3] + 1)
            prev_at_i.append(i // 3)
        if i % 2 == 0:
            ops_at_i.append(min_calcs[i // 2] + 1)
            prev_at_i.append(i // 2)
        if i -1 > 0:
            ops_at_i.append(min_calcs[i - 1] + 1)
            prev_at_i.append(i - 1)

        # temp storage
        min_calcs.append(n)
        previous.append(n)
        for k in range(len(ops_at_i)):
            if ops_at_i[k] < min_calcs[i]:
                min_calcs[i] = ops_at_i[k]
                previous[i] = prev_at_i[k]

    j = n
    sequence = [n]
    while j > 1:
        sequence.append(previous[j])
        j = previous[j]

    sequence.reverse()

    return sequence

if __name__ == '__main__':

    input = sys.stdin.read()
    n = int(input)
    # n = 96234
    sequence = dp_calculator(n)
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
