# Uses python3
import sys
import numpy as np

def optimal_weight(capacity, item_weights):
    """
    Knapsack problem without repetition

    :param W: Total weight
    :param w: list of individual weights
    :return:
    """
    k = np.zeros(shape=[capacity + 1, len(item_weights)])

    # Construct table K(w, j) = maximum value achievable with w weights and j items
    for j in range(len(item_weights)):
        for w in range(capacity + 1):
            if w == 0 or j == 0:
                k[w, j] = 0
            if item_weights[j] > w:
                k[w, j] = k[w, j - 1]
            else:
                k[w, j] = max(k[w, j-1], k[w - item_weights[j], j - 1] + item_weights[j])

    return int(k[w, j])



if __name__ == '__main__':

    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))

    # # Test
    # W = 20
    # w = [4, 5, 5, 6, 6, 6, 10, 9, 8, 8]
    print(optimal_weight(W, w))
