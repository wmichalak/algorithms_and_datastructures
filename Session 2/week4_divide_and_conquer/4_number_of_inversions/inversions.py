# Uses python3
import sys, time
import numpy as np

def get_number_of_inversions(a, b, left, right):
    """

    :param a: list of integers
    :param b: list of zeros to store inversions?
    :param left:
    :param right:
    :return:
    """

    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    return number_of_inversions

def merge_sort_plus_inversions(a):
    """

    :param a: a list of integers
    :return: number of inversions
    """
    inversions = 0
    # print('Splitting ', a)
    if len(a) > 1:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]

        ai = merge_sort_plus_inversions(left)
        bi = merge_sort_plus_inversions(right)
        inversions = ai + bi

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                a[k] = left[i]
                i+=1
            else:
                a[k] = right[j]
                j+=1
                inversions += (len(left)) - i
            k+=1

        while i < len(left):
            a[k]=left[i]
            i+=1
            k+=1

        while j < len(right):
            a[k]=right[j]
            j+=1
            k+=1

    # print("merging ", a)

    return inversions

def getInvCount(arr, n):
    inv_count = 0
    for i in range(n):
        for j in range(i+1,n):
            if (arr[i] > arr[j]):
                inv_count += 1

    return inv_count


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]

    # Testing
    # n = 30000
    # a = [3, 1, 7, 6, 9, 5, 10, 2, 4, 8]
    # n = 5
    # a = [2,3,9,2,9]
    # a = [102, 772, 182, 883, 91, 963]

    # a = np.random.randint(low = 0, high = 1000, size = [1,n])[0].tolist()
    # print(getInvCount(a, n))
    # t0 = time.time()
    inversions = merge_sort_plus_inversions(a)
    # print(time.time() - t0)
    print(inversions)

