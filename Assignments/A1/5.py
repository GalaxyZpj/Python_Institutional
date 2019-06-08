num = []
i = 0
avg = 0
while i < 3:
    x = float(input('Enter number {}: '.format(i+1)))
    avg += x
    num.append(x)
    i += 1
avg /= 3
print(f'Largest number is {max(num):1.2f}')
print(f'Smallest number is {min(num):1.2f}')
print(f'Average is {avg:1.2f}')
