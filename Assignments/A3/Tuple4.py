l = []
while True:
    x = input('Enter data: ')
    if x == '': break
    else: l.append(x)
l.sort()
print(l)
for x in l:
    print(x)
