a, b = map(int, input().split())
c = list(map(int, input().split()))

flg = 0
for i in range(a-1):
    if c[i+1] - c[i] <= b:
        print(c[i+1])
        flg += 1
        break
if flg == 0:
    print(-1)
