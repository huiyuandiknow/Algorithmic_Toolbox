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

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
