# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    if n == 1:
        summands.append(1)
    else:
        i = 1
        while n > 0 and n >= 2*i+1: 
            summands.append(i) 
            n -= i
            i += 1
        if n!= 0:
            summands.append(n)
            
    return summands

if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
