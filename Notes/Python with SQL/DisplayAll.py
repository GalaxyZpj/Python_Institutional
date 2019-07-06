import pymysql as sql
try:
    conn = sql.connect(host = 'localhost', port = 3306, user = 'root', password = '12345678', db = 'Practice')
    cmd = conn.cursor()
    q = "select * from Product2"
    cmd.execute(q)
    rows = cmd.fetchall()
    if rows == None:
        print('Record not found.')
    else:
        for row in rows:
            for cols in row:
                print(cols, end = ' ')
            print()
    conn.close()
except Exception as e:
    print(e)