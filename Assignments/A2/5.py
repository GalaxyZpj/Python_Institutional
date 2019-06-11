s = input()
ss = ''
t = ''
for index, x in enumerate(s):
    if len(ss) == 0:
        print('me1')
        ss += x
    else:
        for i, xi in enumerate(ss):
            print(i, xi)
            if xi < x:
                j = 0
                while ss[j] < x:
                    if ss[j+1] > x:


                    j += 1
                    if j > len(ss) - 1:
                        ss += x
                        break
                    else:



            '''if xi >= x:
                t = ss[i:]
                ss = ss[0:i]
                ss += x
                ss += t
                break
            else:
                while i+1 < len(ss):
                    if ss[i+1] <= x:
                        break
                    else:
                        ss += x
                        break'''

    print(ss)
    print()
print(list(ss))

'''elif len(ss) == 1:
    print('me2')
    if ss[0] > x:
        t = ss[0]
        ss = ss.replace(t, x, 1)
        ss += t
    else:
        ss += x'''




'''for x in s:
    if len(new_s) == 0:
        new_s += x
    elif len(new_s) == 1:
        if new_s[0] > x:
            t = new_s[0]
            new_s = new_s.replace(t, x)
    else:
        i = 0
        while True:
            if x > new_s[i]:
                if x > new_s[i+1]:
                    new_s += x
                    break
                else:
                    t = new_s[i+1]
                    new_s = new_s.replace(new_s[i+1], x, 1)
                    new_s += t
                    break
            else:
                t = new_s[i+1]
                new_s = .replace(new_s[i+1], x, 1)
                new_s += t
'''
