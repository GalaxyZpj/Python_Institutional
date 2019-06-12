def distance(p1,o):
    length = 0
    for x, y in zip(p1, o):
        length += (x-y)**2
    return length**(1/2)
def check_len(p1, p2):
    return distance(p1,o) == distance(p2,o)


n = int(input('Enter no. of dimentions: '))
print('Point1:-')
o = (0,0,0)
t1 = ()
while len(t1) != n:
    t1 += tuple([int(x) for x in input('Enter Dimention: ').split()])
print('Point2:-')
t2 = ()
while len(t2) != n:
    t2 += tuple([int(x) for x in input('Enter Dimention: ').split()])
if check_len(t1, t2):
    print(f'\nThe distance between the points is {distance(t1,t2)}.')
else:
    print('\nThe two points are not equal in length.')
