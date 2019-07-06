import pymysql as sql
try:
    conn = sql.connect(host = 'localhost', port = 3306, user = 'root', password = '12345678', db = 'Practice')
    cmd = conn.cursor()
    id = input('Enter Product ID: ')

    q = f"select * from Product2 where ProductID = {id}"
    cmd.execute(q)
    row = cmd.fetchone()
    if row == None:
        print('Record Not Found.')
    else:
        print(row)
    conn.close()
except Exception as e:
    print(e)