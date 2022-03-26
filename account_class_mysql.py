import sqlite3


class Account:  # mysql?

    id = None

    def __init__(self):

        # create database if it not exists

        conn = sqlite3.connect('accounts_bd_sqlite.db')

        cur = conn.cursor()

        cur.execute('CREATE TABLE IF NOT EXISTS accounts(id INT PRIMARY KEY, cash INT, login TEXT, password TEXT)')

        conn.commit()

        conn.close()

    def sign_up(self, account_data):

        conn = sqlite3.connect('accounts_bd_sqlite.db')

        cur = conn.cursor()

        cur.execute('SELECT MAX(id) FROM accounts')

        row = cur.fetchall()[0][0]

        if row is None:

            self.id = 1

        else:

            self.id = row + 1

        new_user_data = (self.id, 0, account_data[0], account_data[1])

        cur.execute('INSERT INTO accounts(id, cash, login, password) VALUES(?, ?, ?, ?)', new_user_data)

        conn.commit()

        conn.close()

    def sign_in(self, account_data):

        conn = sqlite3.connect('accounts_bd_sqlite.db')

        cur = conn.cursor()

        cur.execute('SELECT id FROM accounts WHERE login = ? and password = ?', account_data)

        row = cur.fetchall()

        conn.close()

        if not row:

            return False

        else:

            self.id = row[0][0]

            return True

    def plus_money(self, amount):

        conn = sqlite3.connect('accounts_bd_sqlite.db')

        cur = conn.cursor()

        cur.execute('SELECT cash FROM accounts WHERE id = ?', (self.id,))

        amount += cur.fetchall()[0][0]

        data = (amount, self.id)

        cur.execute('UPDATE accounts SET cash = ? WHERE id = ?', data)

        conn.commit()

        conn.close()

    def minus_money(self, amount):

        conn = sqlite3.connect('accounts_bd_sqlite.db')

        cur = conn.cursor()

        cur.execute('SELECT cash FROM accounts WHERE id = ?', (self.id,))

        amount = cur.fetchall()[0][0] - amount

        if amount < 0:

            return False

        else:

            data = (amount, self.id)

            cur.execute('UPDATE accounts SET cash = ? WHERE id = ?', data)

            conn.commit()

            conn.close()


account_1 = Account()

account_1.sign_in([input('Enter you login... '), input('Enter you password... ')])
