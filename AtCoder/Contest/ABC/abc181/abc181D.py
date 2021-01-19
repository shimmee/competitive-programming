s = input()

ni = [str(i) for i in range(10, 99) if i % 8 == 0]
ni_re = [i[1]+i[0] for i in ni if i[1] != '0']
for i in ni_re:
    ni.append(i)

eight = [str(i) for i in range(100, 999) if i % 8 == 0]

if len(s) == 1:
    if s == '8':
        print('Yes')
        exit()
    else:
        print('No')
        exit()
elif len(s) == 2:
    if s in ni:
        print('Yes')
        exit()
    else:
        print('No')
        exit()
else:
    for t in eight:
        ori = s
        flag = True
        for i in t:
            new = ori.replace(i, '', 1)
            if len(ori) != len(new):
                ori = new
            else:
                flag = False
        if flag:
            print('Yes')
            exit()
print('No')

