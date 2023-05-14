n = int(input())
s = input()

if s.count('T') == s.count('A') and s[n -1] == 'T':
    print('A')
elif s.count('T') == s.count('A') and s[n -1] == 'A':
    print('T')
elif s.count('T') > s.count('A'):
    print('T')
else:
    print('A')
