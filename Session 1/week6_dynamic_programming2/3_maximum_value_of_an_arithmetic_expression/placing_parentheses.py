# Uses python3
import numpy as np

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):

    num_digits = (len(dataset)+1) // 2
    nums = dataset[::2]
    ops = dataset[1::2]

    # Fill array diagonal with values
    max_array = np.ones(shape=[num_digits, num_digits]) * float('-Inf')
    min_array = np.ones(shape=[num_digits, num_digits]) * float('Inf')

    for i in range(num_digits):
        max_array[i, i] = nums[i]
        min_array[i, i] = nums[i]

    # Fill rest of table, working down diagonals
    i_end = num_digits - 1
    for col_start in range(1, num_digits):
        for row in range(0, i_end):
            col = col_start + row
            # Calculate all possible values
            for k in range(1, col - row + 1):
                # print('*', (row, row + k -1), (row + k, col))
                a = evalt(max_array[row, row + k - 1], max_array[row + k, col], ops[row + k - 1])
                b = evalt(max_array[row, row + k - 1], min_array[row + k, col], ops[row + k - 1])
                c = evalt(min_array[row, row + k - 1], max_array[row + k, col], ops[row + k - 1])
                d = evalt(min_array[row, row + k - 1], min_array[row + k, col], ops[row + k - 1])
                # print(a,b,c,d)
                max_array[row, col] = max([max_array[row, col], a, b, c, d])
                min_array[row, col] = min([min_array[row, col], a, b, c, d])
            # print('----')

        i_end -= 1

    return int(max([max_array[0, col], min_array[0, col]]))

if __name__ == "__main__":
    data = input()
    # data = '5-8+7*4-8+9'
    # data = '1+4*5-6+3'
    print(get_maximum_value(data))
