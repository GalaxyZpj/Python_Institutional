i_grade = input('Enter a grade: ')
try:
    i_grade = int(i_grade)
except:
    print('Enter a valid grade.')
if i_grade <= 10 and i_grade >= 8.5:
    a_grade = 'A'
elif i_grade <= 8 and i_grade >= 7.5:
    a_grade = 'B'
elif i_grade <= 7 and i_grade >= 6.5:
    a_grade = 'C'
elif i_grade <= 6 and i_grade >= 5.5:
    a_grade = 'D'
else:
    a_grade = 'F'
print(f'Grade: {a_grade}')
