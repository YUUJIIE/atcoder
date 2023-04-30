a, b, c = map(int, input().split())
d = list(map(int, input().split()))

for i in range(a):
    if d[i] == b + c:
        print(i + 1)
