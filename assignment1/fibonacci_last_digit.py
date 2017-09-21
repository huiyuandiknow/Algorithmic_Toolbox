# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    else:
        numberList = [0] * n
        numberList[0] = numberList[1] = 1 
        for i in range(2, n):
            numberList[i] = numberList[i-1] % 10 + numberList[i-2] % 10 

    return numberList[n-1] % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
