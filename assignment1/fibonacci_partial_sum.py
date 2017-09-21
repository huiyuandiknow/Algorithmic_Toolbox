# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    if to <= 1:
        return to

    remainders = [0] * (6*10 + 1) # period is bounded by 6m
    remainders[0] = remainders[1] = 1

    # find the period of remainder patterns
    for i in range(2, to+2):
        remainders[i] = ( remainders[i-1] + remainders[i-2] ) % 10
        if remainders[i-2] == 1 and remainders[i-1] == 0 and remainders[i] == 1:  
            # found the period i
            return  remainders[ (to+1) % i] - remainders[ (from_+1) % i] + remainders[ (from_-1) % i]  

    # for values smaller than the period
  #  print(remainders)
  #  print(remainders[to+1])
  #  print(remainders[(from_+1)])
   # print(remainders[(from_ -1)])
    return (remainders[to+1] - remainders[(from_+1)] + remainders[(from_-1)]) % 10 


if __name__ == '__main__':
    input = sys.stdin.readline();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
