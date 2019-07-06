import pymysql as sql

conn = sql.connect(host = 'localhost', port = 3306, user = 'root', password = '12345678', db = 'Practice')
cmd = conn.cursor()
q = "create table Product2 (Productid integer primary key, ProductName varchar (20), ProductRate int, ProductMfd date);"
cmd.execute(q)
print('Table Created')
conn.commit()
conn.close()
