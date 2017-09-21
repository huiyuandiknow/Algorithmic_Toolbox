# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    remainders = [0] * (6*10+ 1) # period is bounded by 6m
    remainders[0] = remainders[1] = 1

    # find the period of remainder patterns
    for i in range(2, n + 2):
        remainders[i] = ( remainders[i-1] + remainders[i-2] ) % 10
        if remainders[i-2] == 1 and remainders[i-1] == 0 and remainders[i] == 1:  
            # f(1)+f(2)+...f(n) = f(n+2) - 1
            result = remainders[(n+1) % i] -1
            if result == -1:
                return 9
            return result # i is the period

    # for values smaller than the period
    return (remainders[n+1]-1) % 10

if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    print(fibonacci_sum_naive(n))
