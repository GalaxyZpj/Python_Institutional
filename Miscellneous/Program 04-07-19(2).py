import pymysql as sql
conn = sql.connect(host = 'localhost', port = 3306, user = 'root', password = '12345678', db = 'Practice')
cmd = conn.cursor()
q = "select * from Customer where AmountDue > 0"
cmd.execute(q)
rows = cmd.fetchall()
print('Customers with Due Amount:-')
for row in rows:
    for col in row:
        print(col, end = ' ')
    print()
conn.commit()
conn.close()
