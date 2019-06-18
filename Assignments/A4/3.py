def invert_dict(d):
    nd = {}
    for x, y in d.items():
        l = []
        if y in nd:
            l += nd[d[x]]
            l.append(x)
        else:
            l.append(x)
        nd[y] = l
    return nd
d = { "key1" : "value1", "key2" : "value2", "key3" : "value1" }
print(invert_dict(d))
