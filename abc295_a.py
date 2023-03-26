n = int(input())
str_list = input().split()
#print(str_list)
yes_flg = 0
for s in str_list:
    #print(s)
    if s == 'and' or s == 'not' or s == 'that' or s== 'the' or s == 'you':
        yes_flg += 1
if yes_flg >= 1:
	print('Yes')
else:
    print('No')
