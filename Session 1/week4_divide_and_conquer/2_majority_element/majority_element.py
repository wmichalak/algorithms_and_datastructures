# Uses python3
import sys
import numpy as np

def get_majority_element(arr, left, right):
    """Find majority element.

    Create an array to add sum of each element. step up the array. for each element count

    :param arr: list of integers
    :param left: starting place to search
    :param right: size of the array

    :return 1 if given number exists >n/2 times (majority) and -1 otherwise
    """

    # Find max in O(n)
    m = 0
    for a in arr:
        if a > m:
            m = a

    counts = np.empty([1,m+1])

    for a in arr:
        counts[0][a] += 1
        if int(counts[0][a]) > int(right/2):
            return 1

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
