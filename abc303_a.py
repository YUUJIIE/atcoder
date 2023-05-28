n = int(input())
a = input()
b = input()

flg = 0

if a == b:
    flg = 0
elif ("1" in a or "l" in a or "0" in a or "o" in a) and ("1" in b or "l" in b or "0" in b or "o" in b):
    for i in range(n):
        if a[i] == b[i]:
            flg += 0
        elif ((a[i] == "1" and b[i] == "l") or (a[i] == "l" and b[i] == "1")) or ((a[i] == "0" and b[i] == "o") or (a[i] == "o" and b[i] == "0")):
            flg += 0
        else:
            flg += 1
else:
    flg = 1
if flg == 0:
    print("Yes")
else:
    print("No")