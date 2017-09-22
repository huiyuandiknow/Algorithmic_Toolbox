# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    unit_price = []
    for i in range(len(weights)):
        unit_price.append(1.*values[i]/weights[i])        
    
    for _ in range(len(weights)):
        i = unit_price.index(max(unit_price)) 
        w = weights[i]
        a = min(capacity, w)
        value += a*unit_price[i]
        weights[i] -= a
        capacity -= a
        unit_price[i] = 0 
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
