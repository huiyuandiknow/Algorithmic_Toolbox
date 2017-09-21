# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0
largest = max(a);
a.remove(largest)
second_largest = max(a)
result = largest * second_largest
print(result)
