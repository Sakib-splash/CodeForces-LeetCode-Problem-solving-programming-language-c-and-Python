n, k = map(int, input().split())
a = list(map(int, input().split()))

t = a[k - 1]       # k-th place score
c = 0
for x in a:
    if x >= t and x > 0:
        c += 1

print(c)
