s = input()
a = 'a'
arr = []

for k, v in enumerate(s):
    #print(v)
    if v == a:
        #print(k)
        i = k + 1
    else:
        i = -1
    arr.append(i)
#print(arr)
ans = max(arr)
print(ans)
