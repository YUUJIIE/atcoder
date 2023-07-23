n = int(input())
s = input()

arr = []
arr.append(s.index('A')+1)
arr.append(s.index('B')+1)
arr.append(s.index('C')+1)

print(max(arr))
