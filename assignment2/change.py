# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = 0 
    while m > 0:
        numberTen = int(m/10)
        if numberTen >= 0:
            coins += numberTen
            m -= numberTen*10
        if m <= 9 and m >= 5:
            coins += 1
            m-= 5
        else:
            coins += m
            m-= m
    return coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
