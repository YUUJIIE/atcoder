s1 = input().split()
s2 = input().split()
arr = []

# print(s1)
# print(s2)

for i in s2:
    # print (i)
    if i > s1[1]:
        arr.append(i)
    else:
        arr.append(0)

print(arr)
