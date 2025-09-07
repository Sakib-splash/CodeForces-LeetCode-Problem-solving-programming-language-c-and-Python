import sys

input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
for _ in range(t):
    k = int(data[index])
    x = int(data[index + 1])
    index += 2
    initial = x * (2 ** k)
    print(initial)