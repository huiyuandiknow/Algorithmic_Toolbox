# Uses python3
import sys

# using the fact that fibonacci numbers mod m exhibit a pattern that repeats (periodic), 
# we can determine the value just by using the period
def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    remainders = [0] * (6*m + 1) # period is bounded by 6m
    remainders[0] = remainders[1] = 1

    # find the period of remainder patterns
    for i in range(2, n):
        remainders[i] = ( remainders[i-1] + remainders[i-2] ) % m
        if remainders[i-2] == 1 and remainders[i-1] == 0 and remainders[i] == 1:  
            # found the period
            return remainders[ (n-1) % i] # i is the period

    # for values smaller than the period 
    return remainders[n-1]

if __name__ == '__main__':
    input = sys.stdin.readline();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))


