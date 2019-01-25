# Uses python3


from math import fmod


def GCD(a=None, b=None):
    """Return the greatest common divisor of two numbers by setting aprime=mod(a,b) and then setting a=aprime until the
     remainder is zero or less"""
    if a is None and b is None:
        ints = input()
        tokens = ints.split()
        a = int(tokens[0])
        b = int(tokens[1])
    ap = a
    while b > 0:
        bold = b
        b = fmod(ap,bold)
        ap = bold
        # print(ap, b)
    print(int(ap))

if __name__ == '__main__':
    # Test cases
    # GCD(18,35)
    # GCD(28851538,1183019)

    GCD()