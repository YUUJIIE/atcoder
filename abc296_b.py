s = [input() for i in range(8)]

ans = ''
col = 'abcdefgh'
n = 8

for i, t in enumerate(s):
    if '*' in t:
        ans += col[t.find('*')]
        ans += str(n - i)
print(ans)
