s = input('Enter a string: ')
ss = '~'
for y in s:
    for i,x in enumerate(ss):
        t1 = ''
        t2 = ''
        if y <= x:
            t1 = ss[:i]
            t2 = ss[i:]
            ss = ''
            ss = t1
            ss += y
            ss += t2
            break
        elif i == len(ss)-1 and y > x:
            ss += x
            break
        else:
            continue
ss = ss[:len(ss)-1]
print('\nSorted String:', ss)
