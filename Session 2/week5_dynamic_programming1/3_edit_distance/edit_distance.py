# Uses python3
import numpy as np

def edit_distance(s, t):
    """

    :param s: string 1
    :param t: string 2
    :return: return integer minimum number of edits
    """

    # Allocate array
    d = np.empty([len(s)+1, len(t)+1])

    # Build array, starting with edges known
    for i in np.arange(0, len(s)+1):
        d[i, 0] = i
    for j in np.arange(0, len(t)+1):
        d[0, j] = j

    for i in np.arange(1, len(s)+1):
        for j in np.arange(1, len(t)+1):
            if s[i-1] == t[j-1]:
                d[i, j] = d[i-1, j-1]
            else:
                d[i, j] = min(d[i, j - 1] + 1,
                              d[i-1, j] + 1,
                              d[i-1, j-1] + 1)


    return int(d[i, j])

if __name__ == "__main__":
    print(edit_distance(input(), input()))
    # Test
    # print(edit_distance('editing', 'distance'))