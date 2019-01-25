# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    """Find the maximal value of items that fit into the backpack
    :param capacity:
    :param weights:
    :param values:
    :return maximum price of items that fit into the backpack of given capacity"""

    # Get price per weight list sorted from most to least valueable
    items = sorted([(p/w, p, w) for p, w in zip(values, weights)], reverse=True)

    total_weight = 0
    total_value = 0

    # try full unit items
    for item in items:
        item_ppw = item[0]
        item_value = item[1]
        item_weight = item[2]
        if total_weight <= capacity:
            if (item_weight + total_weight) <= capacity:
                total_weight += item_weight
                total_value += item_value
            # If discrete items don't fill, add fraction of item until full
            else:
                total_value +=  (capacity - total_weight) * item_ppw
                total_weight += (capacity - total_weight)

    return total_value


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]

    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
