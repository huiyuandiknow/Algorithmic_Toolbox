#Uses python3

import sys

def IsGreaterOrEqual(a, b):
    l1 = len(str(a)); l2 = len(str(b))
    if int(a) + int(b)*(10**l1) > int(b) + int(a)*(10**l2):
        return False
    else:
        return True
    
def largest_number(a):
    #write your code here
    res = ""
    while a != []:
        maxDigit = -999
        for i in a:
            if IsGreaterOrEqual(i,maxDigit): 
                maxDigit = i
        res += str(maxDigit)
        a.remove(maxDigit) 
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
