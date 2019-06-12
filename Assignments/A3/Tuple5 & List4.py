c = ['']*52
count_c = [0]*52
s = input('Enter a string: ')
for i,x in enumerate(s):
    if (x >= 'a' and x <= 'z') or (x >= 'A' and x <= 'Z'):
        if x.upper() not in c and x.lower() not in c:
            c[i] = x.upper()
            count_c[i] = s.count(x.lower()) + s.count(x.upper())
for a, b in zip(c, count_c):
    if a != '':
        print(f"\'{a}\' appears {b} times in given string.")
