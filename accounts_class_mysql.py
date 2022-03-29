from mysql.connector import connect

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

        # create table with login/password data if it not exists

        conn = connect(
            host=server_data[0],
            user=server_data[1],
            password=server_data[2],
            database='accounts_bd_mysql'
        )

        cur = conn.cursor()

        cur.execute(
            '''CREATE TABLE IF NOT EXISTS register_data(
            id INT AUTO_INCREMENT PRIMARY KEY,  
            login VARCHAR(100), 
            password VARCHAR(100)
            )'''
        )

        # create table with cash data if it not exists

        cur.execute(
            '''CREATE TABLE IF NOT EXISTS cash_data(
            id INT AUTO_INCREMENT PRIMARY KEY,
            cash INT,
            FOREIGN KEY (id) REFERENCES register_data(id) ON DELETE CASCADE ON UPDATE CASCADE
            )'''
        )

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

        new_user_data = (account_data[0], account_data[1])

        cur.execute('INSERT INTO register_data(login, password) VALUES(%s, %s)', new_user_data)

        new_user_cash = (0,)

        cur.execute('INSERT INTO cash_data(cash) VALUES(%s)', new_user_cash)

        cur.execute('SELECT MAX(id) FROM register_data')

        self.id = cur.fetchone()[0]

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

        cur.execute('SELECT id FROM register_data WHERE login = %s and password = %s', account_data)

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

        cur.execute('SELECT cash FROM cash_data WHERE id = %s', (self.id,))

        amount += cur.fetchone()[0]

        data = (amount, self.id)

        cur.execute('UPDATE cash_data SET cash = %s WHERE id = %s', data)

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

        cur.execute('SELECT cash FROM cash_data WHERE id = %s', (self.id,))

        amount = cur.fetchone()[0] - amount

        if amount < 0:

            cur.close()

            conn.close()

            return False

        else:

            data = (amount, self.id)

            cur.execute('UPDATE cash_data SET cash = %s WHERE id = %s', data)

            conn.commit()

            cur.close()

            conn.close()


account_1 = Account()

user_data = [input('Enter you login... '), input('Enter you password... ')]

if not account_1.sign_in(user_data):
    account_1.sign_up(user_data)

while True:

    turn = input('"q" if you want quit.\n+ or - ? ')

    if turn == 'q':
        break

    while turn not in ['+', '-']:
        turn = input('Incorrect value!\n"+" or "-" ? ')

    amount = int(input('Amount? '))

    while not type(amount) is int:
        amount = int(input('Incorrect value!\nAmount?(Integer) '))

    if turn == '+':
        account_1.plus_money(amount)

    else:
        account_1.minus_money(amount)

print('Thanks for using.')
