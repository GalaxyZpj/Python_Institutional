for x in range(ord('A'), ord('Z')):
    print(chr(x), end='')
print()
i = 0
for x in range(ord('A')+13, ord('Z')+13):
    if x > ord('Z'):
        print(chr(ord('A')+i), end='')
        i += 1
    else:
        print(chr(x), end='')
print()
