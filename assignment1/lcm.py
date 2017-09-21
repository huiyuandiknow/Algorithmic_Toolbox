# Uses python3
import sys


def gcd_naive(a, b):
    if a > b:
        larger= a; smaller= b
    else:
        smaller = a; larger = b

    while larger % smaller != 0:
        tmp = larger % smaller
        larger = smaller
        smaller = tmp         
        
    return smaller

def lcm_naive(a, b):
    gcd = gcd_naive(a,b)
    return a*(int(b/gcd))
if __name__ == '__main__':
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

