def sum_0(l):
    for index in range(len(l)):
        t = l[:index+1]
        for i in l:
            if i in t: continue
            t[index] = i
            for x in l:
                if x in t: continue
                t.append(x)
                if sum(t) == 0:
                    return t
                t.pop()
l = [int(x) for x in input('Enter numbers: ').split()]
print(sum_0(l))
