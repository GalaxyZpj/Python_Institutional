from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    return render(request, "welcome.html")
def student_view(request):
    return render(request, "student.html")
def student_result(request):

    def assign_grade(m):
        if m >=90: return 'A+'
        elif m >=80: return 'A'
        elif m >=70: return 'B+'
        elif m >=60: return 'B'
        elif m >=50: return 'C+'
        elif m >=40: return 'C'
        elif m >=30: return 'D'
        else: return 'F'

    def assign_remark(g):
        if g == 'F': return 'Fail'
        elif g == 'A+': return 'Distinction'
        else: return 'Pass'

    hindi = int(request.GET['Hindi'])
    english = int(request.GET['English'])
    maths = int(request.GET['Maths'])
    physics = int(request.GET['Physics'])
    chemistry = int(request.GET['Chemistry'])
    ghindi = assign_grade(hindi)
    genglish = assign_grade(english)
    gmaths = assign_grade(maths)
    gphysics = assign_grade(physics)
    gchemistry = assign_grade(chemistry)

    Grades = [ghindi, genglish, gmaths, gphysics, gchemistry]

    if 'F' in Grades:
        if Grades.count('F') > 2: remark = 'FAIL'
        else: remark = 'COMPARTMENT'
    else:
        if Grades.count('A+') > 3: remark = 'DISTINCTION'
        else: remark = 'PASS'

    d = {
        'rollno': request.GET['rn'], 
        'n': request.GET['sn'], 
        'fn': request.GET['fn'], 
        'gender': request.GET['gen'], 
        'schoolname': request.GET['sch'], 
        'hindi': hindi, 
        'english': english, 
        'maths': maths, 
        'physics': physics, 
        'chemistry': chemistry, 
        'ghindi': ghindi, 
        'genglish': genglish, 
        'gmaths': gmaths, 
        'gphysics': gphysics, 
        'gchemistry': gchemistry,
        'rhindi': assign_remark(ghindi), 
        'renglish': assign_remark(genglish), 
        'rmaths': assign_remark(gmaths), 
        'rphysics': assign_remark(gphysics), 
        'rchemistry': assign_remark(gchemistry),
        'remark': remark
    }

    return render(request, "result.html", d)
