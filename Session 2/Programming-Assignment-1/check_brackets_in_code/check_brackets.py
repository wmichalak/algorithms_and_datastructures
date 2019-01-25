# python3
import os
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    if len(text) == 1:
        return 1
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(char=next, position=i))

        if next in ")]}":
            if not opening_brackets_stack:
                return i + 1
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next):
                return i + 1

    if opening_brackets_stack:
        return opening_brackets_stack[0].position + 1
    else:
        return 'Success'

def main():
    text = input()
    print(find_mismatch(text))

    # Testing
    # direc = '/Users/wmichalak/AlgorithmsDataStructures/Session 2/Programming-Assignment-1/check_brackets_in_code/tests'
    # files = os.listdir(direc)
    # filelist = []
    # for f in files:
    #     if '.a' not in f:
    #         filelist.append(f)
    # filelist = sorted(filelist)
    #
    # for i, f in enumerate(filelist):
    #     with open(direc + '/' + f) as fname:
    #         text = fname.readline()
    #         mismatch = find_mismatch(text)
    #
    #         with open(direc + '/' + f +'.a') as fname_answer:
    #             # print(i, text, fname_answer.readline().strip('\n'),   ' a:' + str(mismatch))
    #             print(fname_answer.readline().strip('\n'),   ' a:' + str(mismatch))


if __name__ == "__main__":
    main()
