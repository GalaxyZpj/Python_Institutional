text = "How much wood would a woodchuck chuck If a woodchuck could chuck wood? He would chuck, he would, as much as he could, And chuck as much as a woodchuck would If a woodchuck could chuck wood."
text = text.lower()
for i,x in enumerate(text):
    t1 = ''
    t2 = ''
    if ord(x) not in range(ord('a'), ord('z')+1):
        t1 = text[:i]
        t2 = text[i+1:]
        text = ''
        text += t1
        text += ' '
        text += t2
text = text.split()
count_l = []
l = []
for x in text:
    if x not in l:
        l.append(x)
        count_l.append(text.count(x))
d = {}
for x, y in sorted(zip(count_l, l)):
    d[y] = x
print(d)
