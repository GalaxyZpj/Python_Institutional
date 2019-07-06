import pymysql as sql

conn = sql.connect(host = 'localhost', port = 3306, user = 'root', password = '12345678', db = 'Practice')
cmd = conn.cursor()
print('Enter City Names Seperated By Comma:-')
city = [x for x in input().split(',')]
q = "create table Cities(ID int primary key, CityName varchar(40))"
cmd.execute(q)
for i,x in enumerate(city):
    q = f"insert into Cities values({i+1}, '{x}')"
    cmd.execute(q)
print('Data Added to Database.')
conn.commit()
conn.close()
