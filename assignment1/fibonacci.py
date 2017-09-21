# Uses python3
def calc_fib(n):
    if n <= 1:
        return n
    else:
        numberList = [0] * n
        numberList[0] = numberList[1] = 1 
        for i in range(2, n):
            numberList[i] = numberList[i-1] + numberList[i-2]

    return numberList[n-1]

n = int(input())
print(calc_fib(n))
