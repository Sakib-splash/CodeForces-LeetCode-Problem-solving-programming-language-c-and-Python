import math

n, m, a = map(int, input().split())

# Using math.ceil
flagstones = math.ceil(n / a) * math.ceil(m / a)

print(flagstones)
