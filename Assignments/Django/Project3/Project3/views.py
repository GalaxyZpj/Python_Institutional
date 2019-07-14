from django.shortcuts import render
import pymysql as sql
from datetime import datetime, date, timedelta, time
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
import time
from django.http import HttpResponse

# Rendered Web Pages
def homepage(request):
    return render(request, "base.html")

def initiateSessionView(request):
    return render(request, "InitiateLockerSession.html", {'wall': [0]})

def remote(request):
    return render(request, "Remote.html")

#BackEnd Functions
def redirect(request):
    print(f"\n\n\n{request.GET['goto']}")
    if request.GET['goto'] == 'Base':
        return render(request, "base.html")
    elif request.GET['goto'] == 'customerPortal':
        return render(request, "customerPortal.html")
    elif request.GET['goto'] == 'employeePortal':
        return render(request, "employeePortal.html")
    elif request.GET['goto'] == 'Admin':
        return render(request, "adminPortal.html")
    elif request.GET['goto'] == 'customerLogin':
        return render(request, "customerLogin.html")
    elif request.GET['goto'] == 'employeeLogin':
        return render(request, "employeeLogin.html")
    elif request.GET['goto'] == 'customerRegister':
        return render(request, "customerRegister.html", {'output': ''})
    elif request.GET['goto'] == 'employeeRegister':
        return render(request, "employeeRegister.html")
    # Admin Redirects
    elif request.GET['goto'] == 'SearchCustomer':
        return render(request, "searchCustomer.html", {'x': ''})
    elif request.GET['goto'] == 'ShowCustomer':
        return render(request, "showCustomer.html")
    elif request.GET['goto'] == 'SearchEmployee':
        return render(request, "searchEmployee.html", {'x': ''})
    elif request.GET['goto'] == 'ShowEmployee':
        return render(request, "showEmployee.html")

def registration(request):
    # Linking to database
    conn = sql.connect(host = 'localhost', port = 3306, user = 'root', password = '12345678', db = 'BankLocker')
    cmd = conn.cursor()
    entry = request.GET['register']
    if entry == 'cRegister':
        accno = request.GET['accno']
        first_name = request.GET['fn']
        last_name = request.GET['ln']
        dob = request.GET['dob']
        try: gender = request.GET['gen']
        except: gender = ''
        mobile = request.GET['mob']
        email = request.GET['email']
        status = 'Not Active'
        password = request.GET['pass']
        pin = request.GET['pin']
        adminVerified = 'No'
        entryValidator = 'Not Allowed'
        # Setting current date and date one year later
        dateToday = date.today()
        dateLaterOneYear = dateToday + timedelta(days = 365)
        if accno == '' or first_name == '' or last_name == '' or dob == '' or gender == '' or mobile == '' or email == '' or password == '' or pin == '':
            return render(request, "customerRegister.html", {'output': 'Fill all required entries.'})
        q = f"insert into CustomerData values({accno}, '{first_name}', '{last_name}', '{dob}', '{gender}', '{mobile}', '{email}', '{dateToday.strftime('%Y-%m-%d')}', '{dateLaterOneYear.strftime('%Y-%m-%d')}', '{status}', '{password}', '{pin}', '{adminVerified}', '{entryValidator}')"
        cmd.execute(q)
        conn.commit()
        conn.close()
        return render(request, "customerRegister.html", {'output': 'Record Submitted Successfully.'})
    elif entry == 'eRegister':
        employeeID = request.GET['employeeID']
        name = request.GET['name']
        dob = request.GET['dob']
        try: gender = request.GET['gen']
        except: gender = ''
        designation = request.GET['designation']
        email = request.GET['email']
        password = request.GET['pass']
        mobile = request.GET['mob']
        address = request.GET['address']
        city = request.GET['city']
        state = request.GET['state']
        adminVerified = 'No'
        if employeeID == '' or name == '' or dob == '' or gender == '' or designation == '' or mobile == '' or email == '' or password == '' or address == '' or city == '' or state == '':
            return render(request, "employeeRegister.html", {'output': 'Fill all required entries.'})
        q = f"insert into EmployeeData values({employeeID}, '{name}', '{dob}', '{gender}', '{designation}', '{email}', '{password}', '{mobile}', '{address}', '{city}', '{state}', '{adminVerified}')"
        cmd.execute(q)
        conn.commit()
        conn.close()
        return render(request, "employeeRegister.html", {'output': 'Record Submitted Successfully.'})

def loginCheck(request):
    conn = sql.connect(host = 'localhost', port = 3306, user = 'root', password = '12345678', db = 'BankLocker')
    cmd = conn.cursor()
    entry = request.GET['login']
    if entry == 'cLogin':
        accno = request.GET['c_accno']
        password = request.GET['c_pass']
        if accno == '' or password == '': return render(request, 'customerLogin.html', {'login': 'Enter All Required Fields.'})
        q = f"select AccountNo, Password, AdminVerified from CustomerData where AccountNo='{accno}'"
        cmd.execute(q)
        row = cmd.fetchone()
        q = f"select * from CustomerData where AccountNo='{accno}'"
        cmd.execute(q)
        session = cmd.fetchone()
        s = []
        for r in session:
            s.append(r)
        print('\n\n\n', s)
        for x in [3, 7, 8]:
            s[x] = s[x].strftime('%Y-%m-%d')
        request.session['SES'] = s
        conn.close()
        if row==None: return render(request, 'customerLogin.html', {'login': 'Account Number Doesnot Exist.   Please consider registering first.'})
        if row[2] != 'Yes': return render(request, 'customerLogin.html', {'login': 'Account not verified by the Administrator, Please contact your bank.'})
        if row[1] == password and str(row[0]) == accno: return render(request, 'customerDashboard.html')
        else: return render(request, 'customerLogin.html', {'login': 'Invalid Credentials'})
    elif entry == 'eLogin':
        email = request.GET['email']
        password = request.GET['password']
        if email == '' or password == '': return render(request, 'employeeLogin.html', {'login': 'Enter All Required Fields.'})
        q = f"select Password, AdminVerified from EmployeeData where Email = '{email}'"
        cmd.execute(q)
        row = cmd.fetchone()
        conn.close()
        request.session['EMP'] = row
        if row==None: return render(request, 'employeeLogin.html', {'login': 'Email Doesnot Exist.   Please consider registering first.'})
        if row[1] != 'Yes': return render(request, 'employeeLogin.html', {'login': 'You have not been verified as an Employee, Please contact the Admin.'})
        if row[0] == password: return render(request, "employeeDashboard.html")
        else: return render(request, 'employeeLogin.html', {'login': 'Invalid Credentials'})
    elif entry == 'aLogin':
        masterkey = request.GET['masterkey']
        if masterkey == '': return render(request, 'adminPortal.html', {'login': 'Enter the MasterKey.'})
        q = f"select Password from EmployeeData where Name = 'ADMIN'"
        cmd.execute(q)
        row = cmd.fetchone()
        conn.close()
        if row[0] == masterkey: return render(request, "adminDashboard.html")
        else: return render(request, 'adminPortal.html', {'login': 'MasterKey Incorrect,  Login RESTRICTED!'})

def searchCustomer(request):

    accno = request.GET['s_accno']
    if accno == '': return render(request, "searchCustomer.html", {'err': 'Please enter Account Number to fetch record.', 'x': ''})
    # Linking to database
    conn = sql.connect(host = 'localhost', port = 3306, user = 'root', password = '12345678', db = 'BankLocker')
    cmd = conn.cursor()
    try: setVerify = request.GET['setVerify']
    except: setVerify = ''
    if setVerify != '':
        q = f"update CustomerData set AdminVerified = 'Yes' where AccountNo = {setVerify}"
        cmd.execute(q)
        q = f"select Status, ValidTillDate from CustomerData where AccountNo = {setVerify}"
        cmd.execute(q)
        status = cmd.fetchone()
        if status[0] != 'Active':
            if status[1] > date.today():
                q = f"update CustomerData set Status = 'Active' where AccountNo = {setVerify}"
                cmd.execute(q)
        conn.commit()
    q = f"select * from CustomerData where AccountNo = {accno}"
    try: cmd.execute(q)
    except: return render(request, "searchCustomer.html", {'err': 'Record Not Found.', 'x': ''})
    row = cmd.fetchone()
    if row == None: return render(request, "searchCustomer.html", {'err': 'Record Not Found.', 'x': ''})
    print('\n\n\n\n\n',row)
    conn.close()

    # Rendering Webpage
    return render(request, "searchCustomer.html", {'x': row})

def showCustomers(request):
    # Linking to database
    conn = sql.connect(host = 'localhost', port = 3306, user = 'root', password = '12345678', db = 'BankLocker')
    cmd = conn.cursor()
    try: setVerify = request.GET['setVerify']
    except: setVerify = ''
    if setVerify != '':
        q = f"update CustomerData set AdminVerified = 'Yes' where AccountNo = {setVerify}"
        cmd.execute(q)
        q = f"select Status, ValidTillDate from CustomerData where AccountNo = {setVerify}"
        cmd.execute(q)
        status = cmd.fetchone()
        if status[0] != 'Active':
            if status[1] > date.today():
                q = f"update CustomerData set Status = 'Active' where AccountNo = {setVerify}"
                cmd.execute(q)
        conn.commit()
    q = f"select * from CustomerData"
    cmd.execute(q)
    row = cmd.fetchall()
    Row = []
    for r in row:
        t = []
        for c in r:
            t.append(c)
        Row.append(t)
    row = Row
    if len(row) == 0: return render(request, "showCustomer.html", {'d': row, 'err': 'No Records.'})
    return render(request, "showCustomer.html", {'d': row, 'err': ''})

def searchEmployee(request):
    email = request.GET['email']
    if email == '': return render(request, "searchEmployee.html", {'err': 'Please enter Email to fetch record.', 'x': ''})
    # Linking to database
    conn = sql.connect(host = 'localhost', port = 3306, user = 'root', password = '12345678', db = 'BankLocker')
    cmd = conn.cursor()
    try: setVerify = request.GET['setVerify']
    except: setVerify = ''
    if setVerify != '':
        q = f"update EmployeeData set AdminVerified = 'Yes' where Email = '{setVerify}'"
        cmd.execute(q)
        conn.commit()
    q = f"select * from EmployeeData where Email = '{email}'"
    try: cmd.execute(q)
    except: return render(request, "searchEmployee.html", {'err': 'Record Not Found.', 'x': ''})
    row = cmd.fetchone()
    if row == None: return render(request, "searchEmployee.html", {'err': 'Record Not Found.', 'x': ''})
    print('\n\n\n\n\n',row)
    conn.close()

    # Rendering Webpage
    return render(request, "searchEmployee.html", {'x': row})

def showEmployees(request):
    # Linking to database
    conn = sql.connect(host = 'localhost', port = 3306, user = 'root', password = '12345678', db = 'BankLocker')
    cmd = conn.cursor()
    try: setVerify = request.GET['setVerify']
    except: setVerify = ''
    if setVerify != '':
        q = f"update EmployeeData set AdminVerified = 'Yes' where Email = '{setVerify}'"
        cmd.execute(q)
        conn.commit()
    q = f"select * from EmployeeData"
    cmd.execute(q)
    row = cmd.fetchall()
    Row = []
    for r in row:
        t = []
        for c in r:
            t.append(c)
        Row.append(t)
    row = Row
    row.pop(0)
    if len(row) == 0: return render(request, "showEmployee.html", {'d': row, 'err': 'No Records.'})
    return render(request, "showEmployee.html", {'d': row, 'err': ''})

def initiateLockerSession(request):
    accno = request.GET['accno']
    if accno == '': return render(request, "initiateLockerSession.html", {'wall': [0], 'accno': accno, 'msg': 'Please Enter Account Number'})
    operation = request.GET['send']
    startTime = datetime.now().strftime('%H:%M:%S')
    onDate = datetime.now().strftime('%Y:%m:%d')
    request.session['LOCKER'] = [accno, onDate, startTime]
    if operation == 'Start':
        conn = sql.connect(host = 'localhost', port = 3306, user = 'root', password = '12345678', db = 'BankLocker')
        cmd = conn.cursor()
        q = f"select AdminVerified from CustomerData where AccountNo='{accno}'"
        cmd.execute(q)
        row = cmd.fetchone()
        if row[0] != 'Yes': return render(request, "initiateLockerSession.html", {'wall': [0], 'accno': accno, 'msg': 'Account not verified by the Administrator'})
        q = f"insert into LockerSession(AccountNo, EmployeeID, Date, StartTime) values({accno}, {request.session['EMP'][0]}, '{onDate}', '{startTime}')"
        cmd.execute(q)
        q = f"update CustomerData set EntryValidator = 'Allowed' where AccountNo = {accno}"
        cmd.execute(q)
        conn.commit()
        q = f"select TransactionID from LockerSession where AccountNo = {accno} and Date = '{request.session['LOCKER'][1]}' and StartTime = '{request.session['LOCKER'][2]}'"
        cmd.execute(q)
        t = cmd.fetchone()
        request.session['LOCKER'].append(t[0])
        request.session['LOCKER_QUIT'] = request.session['LOCKER']
        conn.close()
        return render(request, "initiateLockerSession.html", {'wall': ['True'], 'accno': accno, 't': t})
    elif operation == 'Stop':
        conn = sql.connect(host = 'localhost', port = 3306, user = 'root', password = '12345678', db = 'BankLocker')
        cmd = conn.cursor()
        q = f"update LockerSession set StopTime = '{datetime.now().strftime('%H:%M:%S')}' where TransactionID = {request.session['LOCKER_QUIT'][3]}"
        cmd.execute(q)
        q = f"update CustomerData set EntryValidator = 'Not Allowed' where AccountNo = {request.session['LOCKER'][0]}"
        cmd.execute(q)
        conn.commit()
        conn.close()
        del request.session['LOCKER']
        del request.session['LOCKER_QUIT']
        return render(request, "initiateLockerSession.html", {'wall': [0], 'accno': accno, 'msg': 'Session Ended'})

def connect(s='open'):
    pc=PNConfiguration()
    pc.subscribe_key="sub-c-88748fa0-9c8c-11e9-ab0f-d62d90a110cf"
    pc.publish_key="pub-c-9687c108-59d1-4d77-a4f7-289f64564b77"
    pc.ssl=True
    pubnub = PubNub(pc)
    # Listen for Messages on the Market Order Channel
    channel = 'lock'
    def show(msg,stat):
        if(msg and stat):print(msg.timetoken,stat.status_code)
        else:
            print("Error",stat and stat.status_code)
    pubnub.publish().channel(channel).message('Open').pn_async(show)
    time.sleep(2)
    return HttpResponse("<html><center><h1>UNLOCKED</h1></center></html>")
