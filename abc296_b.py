s = [input() for i in range(8)]
#print(s)

ans = ''
n = 8

for i, t in enumerate(s):
    #print(i)
    if '*' in t:
        ans += str(n - i)
        #print(ans)
        #print('*')
        #print(t.find('*'))
        if t.find('*') == 0:
            ans += 'a'
        elif t.find('*') == 1:
            ans += 'b'
        elif t.find('*') == 2:
            ans += 'c'
        elif t.find('*') == 3:
            ans += 'd'
        elif t.find('*') == 4:
            ans += 'e'
        elif t.find('*') == 5:
            ans += 'f'
        elif t.find('*') == 6:
            ans += 'g'
        elif t.find('*') == 7:
            ans += 'h'

print(ans[::-1])
