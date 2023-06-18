n = list(map(int, input().split()))

arr = []
for i in range(len(n)):
    arr.append(n[i]*2**i)

print(sum(arr))
