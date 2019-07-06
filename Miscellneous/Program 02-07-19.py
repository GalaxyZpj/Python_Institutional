import pymysql as sql

con = sql.connect(host = 'localhost', port = 3306, user = 'root', password = '12345678', db = 'Practice')
cmd = con.cursor()
# q = "create table Customer(CustomerID int primary key, Name varchar(40), Gender char(10), City varchar(30), DOB date, AmountDue int, AmountPaid int)"
# cmd.execute(q)
#q = "insert into Customer values(1, 'Pranav', 'Male', 'Gwalior', '2000-09-19', 0, 172000)"
q = "select * from Products"
cmd.execute(q)
con.commit()
con.close()