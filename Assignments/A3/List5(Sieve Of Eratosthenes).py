###########################
#   Sieve Of Eratosthenes
###########################
n = int(input('Enter a Number: '))
L = []
for x in range(n):
    L.append(x+1)
L[L.index(1)] = 0
for x in L:
    if x is 0:
        continue
    else:
        for y in L:
            if y%x == 0 and y != x:
                #y = 0
                L[L.index(y)] = 0
while 0 in L:
    L.remove(0)
print(f'Prime Numbers Between 1 and {n}: ', L)
