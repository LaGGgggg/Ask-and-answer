from mysql.connector import Error, connect
from getpass import getpass

server_data = ['localhost', 'root', '123asd159ZXC']


class Account:

    id = None

    def __init__(self):

        # create database if not exists

        conn = connect(
            host=server_data[0],
            user=server_data[1],
            password=server_data[2]
        )

        cur = conn.cursor()

        cur.execute('SHOW DATABASES')

        row = cur.fetchall()

        if 'accounts_bd_mysql' not in row[0]:
            cur.execute('CREATE DATABASE accounts_bd_mysql')

            conn.commit()

        cur.close()

        conn.close()

        # create table if it not exists

        conn = connect(
            host=server_data[0],
            user=server_data[1],
            password=server_data[2],
            database='accounts_bd_mysql'
        )

        cur = conn.cursor()

        cur.execute(
            '''CREATE TABLE IF NOT EXISTS accounts(
            id INT AUTO_INCREMENT PRIMARY KEY, 
            cash INT, 
            login VARCHAR(100), 
            password VARCHAR(100)
            )'''
        )  # TODO разнести в две отдельные таблицы

        conn.commit()

        cur.close()

        conn.close()

    def sign_up(self, account_data):

        conn = connect(
            host=server_data[0],
            user=server_data[1],
            password=server_data[2],
            database='accounts_bd_mysql'
        )

        cur = conn.cursor()

        new_user_data = (0, account_data[0], account_data[1])

        cur.execute('INSERT INTO accounts(cash, login, password) VALUES(%s, %s, %s)', new_user_data)

        cur.execute('SELECT MAX(id) FROM accounts')

        self.id = cur.fetchall()[0]

        conn.commit()

        cur.close()

        conn.close()

    def sign_in(self, account_data):

        conn = connect(
            host=server_data[0],
            user=server_data[1],
            password=server_data[2],
            database='accounts_bd_mysql'
        )

        cur = conn.cursor()

        cur.execute('SELECT id FROM accounts WHERE login = %s and password = %s', account_data)

        row = cur.fetchone()

        cur.close()

        conn.close()

        if not row:

            return False

        else:

            self.id = row[0]

            return True

    def plus_money(self, amount):

        conn = connect(
            host=server_data[0],
            user=server_data[1],
            password=server_data[2],
            database='accounts_bd_mysql'
        )

        cur = conn.cursor()

        cur.execute('SELECT cash FROM accounts WHERE id = %s', (self.id,))

        amount += cur.fetchone()[0]

        data = (amount, self.id)

        cur.execute('UPDATE accounts SET cash = %s WHERE id = %s', data)

        conn.commit()

        cur.close()

        conn.close()

    def minus_money(self, amount):

        conn = connect(
            host=server_data[0],
            user=server_data[1],
            password=server_data[2],
            database='accounts_bd_mysql'
        )

        cur = conn.cursor()

        cur.execute('SELECT cash FROM accounts WHERE id = %s', (self.id,))

        amount = cur.fetchone()[0] - amount

        if amount < 0:

            cur.close()

            conn.close()

            return False

        else:

            data = (amount, self.id)

            cur.execute('UPDATE accounts SET cash = %s WHERE id = %s', data)

            conn.commit()

            cur.close()

            conn.close()


account_1 = Account()

account_1.sign_in([input('Enter you login... '), input('Enter you password... ')])
account_1.plus_money(1002)
account_1.minus_money(1000)
