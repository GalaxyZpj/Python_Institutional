import pymysql as sql
try:
    conn = sql.connect(host = 'localhost', port = 3306, user = 'root', password = '12345678', db = 'Practice')
    cmd = conn.cursor()
    id = input('Enter Product ID to be deleted: ')
    q = f"delete from Product2 where ProductID = {id}"
    cmd.execute(q)
    print('Record Deleted.')
    conn.commit()
    conn.close()
except Exception as e:
    print(e)
