from mysql.connector import Error, connect
from getpass import getpass

conn = connect(host='localhost', user='root', password='123asd159ZXC')

cur = conn.cursor()

cur.execute('SHOW DATABASES')

row = cur.fetchall()

if 'accounts_bd_mysql' not in row[0]:

    cur.execute('CREATE DATABASE accounts_bd_mysql')

    conn.commit()

cur.close()

conn.close()

conn = connect(host='localhost', user='root', password='123asd159ZXC', database='accounts_bd_mysql')

cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS accounts(
            id INT AUTO_INCREMENT PRIMARY KEY, 
            cash INT, 
            login VARCHAR(100), 
            password VARCHAR(100)
            )''')  # TODO разнести в две отдельные таблицы

conn.commit()

cur.close()  # TODO ?

conn.close()
