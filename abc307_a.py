n = int(input())
n2 = list(map(int, input().split()))

r = 7
arr = []

weekly = [n2[idx:idx + r] for idx in range(0,len(n2), r)]

for i in range(n):
    arr.append(sum(weekly[i]))

print(*arr)