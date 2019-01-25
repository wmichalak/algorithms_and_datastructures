#Uses python3

import sys,time

def largest_number(a):
    a = list(map(str, sorted(list(map(int, a)), reverse=True)))
    tens = []
    if '10' in a:
        while '10' in a:
            tens.append(a.pop(a.index('10')))
        a += tens

    salary = a[0]
    for x in a[1:]:
       if (x + salary) > (salary + x):
           salary = x + salary
       else:
           salary = salary + x

    return salary

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

