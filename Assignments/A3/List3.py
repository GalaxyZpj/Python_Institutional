queue = []
def dequeue():
    if len(queue) == 0:
        print('Queue Underflow.')
    else:
        print(f'{queue[0]} Removed.')
        queue.pop(0)

def enqueue():
    e = input('Enter Element: ')
    if e == '':
        quit()
    elif e == '?':
        dequeue()
    elif e == 'display()':
        display()
    else:
        queue.append(e)
        print('Element Added.')

def display():
    print(queue)

while True:
    enqueue()
