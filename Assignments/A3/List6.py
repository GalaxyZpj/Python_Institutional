def infinite_for(t, l):
    for i in l:
        if i in t: continue
        t.append(i)
        if sum(t) == 0:
            return (t, True)
        t.pop()
    return (t, False)

def sum_0(l):
    for index in range(len(l)):
        t = l[:index+1]
        for i in l:
            #if i in t: continue
            t[index] = i
            r = infinite_for(t, l)
            if r[1]:
                return r[0]
l = [int(x) for x in input('Enter numbers: ').split()]
print(sum_0(l))
