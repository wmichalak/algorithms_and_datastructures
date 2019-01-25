# python3

import sys, os
import threading
from collections import namedtuple


def compute_height0(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(int(n)):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height

def compute_height(n, parents):

    max_h = 0
    visited = [False] * int(n)
    height = [0] * int(n)

    for i, v in enumerate(parents):
        if visited[i] == False:
            fill_height(parents, i, visited, height)
        max_h = max(max_h, height[i])

    return max_h + 1

def fill_height(p, node, visited, height):

    if p[node] == -1:
        visited[node] = True
        return 0

    if visited[node] == True:
        return height[node]

    visited[node] = True

    new_height = fill_height(p, p[node], visited, height)
    height[node] = 1 + new_height

    return height[node]

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))

    # Testing
    # direc = '/Users/wmichalak/AlgorithmsDataStructures/Session 2/Programming-Assignment-1/tree_height/tests'
    # files = os.listdir(direc)
    # filelist = []
    # for f in files:
    #     if '.a' not in f:
    #         filelist.append(f)
    # filelist = sorted(filelist)
    #
    # for i, f in enumerate(filelist):
    #     with open(direc + '/' + f) as fname:
    #         n = fname.readline()
    #         parents = list(map(int, fname.readline().split()))
    #         height = compute_height(n, parents)
    #
    #         with open(direc + '/' + f +'.a') as fname_answer:
    #             # print(i, parents, fname_answer.readline().strip('\n'),   ' a:' + str(mismatch))
    #             print(i+1, ': ', "true: ", fname_answer.readline().strip('\n'),   '| computed: ' + str(height))

    # print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
