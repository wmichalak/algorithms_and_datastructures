
def ls(A, i):

     LIS = [1] * len(A)
     prev = [-1] * len(A)

     # Generate tables for LIS number and previous index for LIS
     for i in range(len(A)):
         for j in range(i):
             if A[j] < A[i] and LIS[i] < LIS[j] + 1:
                 LIS[i] = LIS[j] + 1
                 prev[i] = j

    # Generate the actual LIS for a given index, i
     j = len(LIS) - 1
     sequence = [A[i]]
     while j > 0:
         sequence.append(A[prev[j]])
         j = prev[j]

     return sequence

if __name__ == '__main__':
    # A = [7, 2, 1, 3, 8, 4, 9 , 1, 2, 6, 5, 9, 3]
    A = [10,22,9,33,21,50,41,60]

    print(ls(A, 7))

    # print(max(lis(A,i) for i in range(len(A))))