def average(l):
    return sum(l)/len(l)

def get_avg(stu_d):
    homework = sum(stu_d['homework'])/len(stu_d['homework'])
    quizzes = sum(stu_d['quizzes'])/len(stu_d['quizzes'])
    tests = sum(stu_d['tests'])/len(stu_d['tests'])
    return homework*0.1 + quizzes*0.3 + tests*0.6

def get_letter_grade(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 60: return 'D'
    else: return 'F'

def get_class_avg(students):
    results = []
    for x in students:
        if x == 'tyler': d = tyler.copy()
        elif x == 'lloyd': d = lloyd.copy()
        elif x == 'alice': d = alice.copy()
        results.append(get_avg(d))
    return sum(results)/len(results)

lloyd = {
	"name": "Lloyd",
	"homework": [90.0,97.0,75.0,92.0],
	"quizzes": [88.0,40.0,94.0],
	"tests": [75.0,90.0]
}
alice = {
	"name": "Alice",
	"homework": [100.0, 92.0, 98.0, 100.0],
	"quizzes": [82.0, 83.0, 91.0],
	"tests": [89.0, 97.0]
}
tyler = {
	"name": "Tyler",
	"homework": [0.0, 87.0, 75.0, 22.0],
	"quizzes": [0.0, 75.0, 78.0],
	"tests": [100.0, 100.0]
}
students = ['lloyd', 'alice', 'tyler']

for x in students:
    if x == 'tyler': d = tyler.copy()
    elif x == 'lloyd': d = lloyd.copy()
    elif x == 'alice': d = alice.copy()
    print('Name: ', d['name'])
    print('Homework: ', d['homework'])
    print('Quizzes: ', d['quizzes'])
    print('Tests: ', d['tests'])
    print('\n')
print('Students List: ', students)
print('Class Average: ', get_class_avg(students))
print('Class Grade: ', get_letter_grade(get_class_avg(students)))
