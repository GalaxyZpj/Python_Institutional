from random import choice

pit = [choice(range(1, 49)) for _ in range(6)]
l = []
for _ in range(6):
    x = int(input('Enter a Number: '))
    if x in pit:
        print(f'Congrats, {x} Accepted!!\n')
        l.append(x)
if len(l) == 0:
    print(pit)
    print('Winnings: 0')
else:
    print('Winnings:', len(l))
