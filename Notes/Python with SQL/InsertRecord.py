import pymysql as sql
try:
    conn = sql.connect(host = 'localhost', port = 3306, user = 'root', password = '12345678', db = 'Practice')
    cmd = conn.cursor()
    pid = input('Enter Product ID: ')
    pn = input('Enter Product Name: ')
    pp = input('Enter Product Price: ')
    pd = input('Enter Product Mfd: ')
    q = "insert into Product2 values({}, '{}', {}, '{}')".format(pid, pn, pp, pd)
    cmd.execute(q)
    print('Record Submitted.')
    conn.commit()
    conn.close()
except Exception as e:
    print(e)