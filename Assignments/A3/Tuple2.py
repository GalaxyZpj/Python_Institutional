def complex_Add():
    complex1 = (int(input('Enter Real Part: ')), int(input('Enter Imaginary Part: ')))
    print(f'Complex Number 1: {complex1[0]} + {complex1[1]}i')
    complex2 = (int(input('Enter Real Part: ')), int(input('Enter Imaginary Part: ')))
    print(f'Complex Number 2: {complex1[0]} + {complex1[1]}i')
    print(f'The Multiplication of following complex numbers is: {complex1[0]*complex2[0] - complex2[1]*complex1[1]} + {complex1[0]*complex2[1] + complex2[0]*complex1[1]}i')
complex_Add()
