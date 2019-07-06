from django.shortcuts import render
import pymysql as sql
from datetime import date, timedelta

def homepage(request):
    return render(request, "base.html")

def redirect(request):
    if request.GET['goto'] == 'Register':
        return render(request, "form.html")
    else:
        return render(request, "search.html")

def searchRecord(request):
    def statusCheck(n, l):
        if n > l: return 'Not Active'
        else: return 'Active'

    accno = request.GET['s_accno']
    password = request.GET['s_pass']

    # Linking to database
    conn = sql.connect(host = 'localhost', port = 3306, user = 'root', password = '12345678', db = 'Practice')
    cmd = conn.cursor()
    q = f"select AccountNo, FirstName, LastName, DOB, Gender, MobileNo, Email, AssignDate, ValidTillDate from BankLocker where AccountNo = {accno} and Password = '{password}'"
    cmd.execute(q)
    row = cmd.fetchone()
    #if row == None: return render(request, "")
    print(row)
    d = {
        's_accno': row[0],
        's_fn': row[1],
        's_ln': row[2],
        's_dob': row[3],
        's_gen': row[4],
        's_mob': row[5],
        's_email': row[6],
        's_assignDate': row[7],
        's_valid': row[8],
        's_status': statusCheck(row[7], row[8])
    }
    conn.close()

    # Rendering Webpage
    return render(request, "searchOutput.html", d)

def formToDatabase(request):
    # Encoding password
    password = request.GET['pass']
    #password = str(password.encode(encoding='UTF-8'))

    # Setting current date and date one year later
    dateToday = date.today()
    dateLaterOneYear = dateToday + timedelta(days = 365)

    # Linking to database
    conn = sql.connect(host = 'localhost', port = 3306, user = 'root', password = '12345678', db = 'Practice')
    cmd = conn.cursor()
    q = f"insert into BankLocker values({request.GET['accno']}, '{request.GET['fn']}', '{request.GET['ln']}', '{request.GET['dob']}', '{request.GET['gen']}', '{request.GET['mob']}', '{request.GET['email']}', '{dateToday.strftime('%Y-%m-%d')}', '{dateLaterOneYear.strftime('%Y-%m-%d')}', 'Active', '{password}')"
    cmd.execute(q)
    conn.commit()
    conn.close()

    # Rendering Webpage
    return render(request, "output.html")
