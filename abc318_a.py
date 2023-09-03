import math
n = list(map(int, input().split()))

ans = (n[0] - n[1]) / n[2]

print(math.floor(ans + 1))