# Uses python3
import sys, math

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l
    return a*b

def lcm_fast(a, b):

    assert(a >= 1)
    assert(b <= 2e9)
    return int((a*b // GCD(a, b)))

def GCD(a, b):
    """Return the greatest common divisor of two numbers by setting aprime=mod(a,b) and then setting a=aprime until the
     remainder is zero or less"""

    ap = a
    while b > 0:
        bold = b
        # b = math.fmod(ap,bold)
        b = ap % bold
        ap = bold
        # print(ap, b)
    return ap

if __name__ == '__main__':
    ints = input()
    tokens = ints.split()
    a = int(tokens[0])
    b = int(tokens[1])

    # print(lcm_naive(a, b))
    print(lcm_fast(a, b))

