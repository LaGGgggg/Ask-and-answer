# Django:

from django.shortcuts import render
from .forms import *

# mysql:

from mysql.connector import connect

# server data for mysql

server_data = ['localhost', 'root', '123asd159ZXC']


def sign_in(request):

    if request.method == 'POST':

        user_form = SignInForm(request.POST)

        if user_form.is_valid():

            user_data = (user_form.cleaned_data['login'], user_form.cleaned_data['password'])

            conn = connect(
                host=server_data[0],
                user=server_data[1],
                password=server_data[2],
                database='accounts_bd_mysql',
            )

            cur = conn.cursor()

            cur.execute('SELECT id FROM register_data WHERE login = %s and password = %s', user_data)

            user_id = cur.fetchone()

            if user_id is None:

                # no account in database

                cur.close()

                conn.close()

                return render(request, 'home_page/sign_in.html', {'form': user_form,
                                                                  'comment': 'Invalid login or password, try again'})

            else:

                cur.execute('SELECT cash FROM cash_data WHERE id = %s', user_id)

                user_cash = cur.fetchone()[0]

                cur.close()

                conn.close()

                # account in database, return account page

                render_data = {
                    'user_id': user_id[0],
                    'login': user_data[0],
                    'password': user_data[1],
                    'cash': user_cash,
                }

                return render(request, 'home_page/user_account.html', {'data': render_data})

        else:

            # invalid user data page

            return render(request, 'home_page/sign_in.html', {'form': user_form})

    else:

        # standard data input page

        user_form = SignInForm()

        return render(request, 'home_page/sign_in.html', {'form': user_form})


def sign_up(request):

    if request.method == 'POST':

        user_form = SignUpForm(request.POST)

        # check on valid and password match

        if user_form.is_valid() and user_form.cleaned_data['password'] == user_form.cleaned_data['password_confirm']:

            user_data = (user_form.cleaned_data['login'], user_form.cleaned_data['password'])

            conn = connect(
                host=server_data[0],
                user=server_data[1],
                password=server_data[2],
                database='accounts_bd_mysql',
            )

            cur = conn.cursor()

            # add user to register_data and cash_data table

            cur.execute('INSERT INTO register_data(login, password) VALUES(%s, %s)', user_data)

            new_user_cash = (0,)

            cur.execute('INSERT INTO cash_data(cash) VALUES(%s)', new_user_cash)

            cur.execute('SELECT id FROM register_data WHERE login = %s and password = %s', user_data)

            user_id = cur.fetchone()[0]

            conn.commit()

            cur.close()

            conn.close()

            render_data = {
                'user_id': user_id,
                'login': user_data[0],
                'password': user_data[1],
                'cash': new_user_cash[0],
            }

            return render(request, 'home_page/user_account.html', {'data': render_data})

        else:

            # invalid user data page

            return render(request, 'home_page/sign_up.html', {'form': user_form, 'comment': "Passwords didn't match."})

    else:

        # standard data input page

        user_form = SignUpForm()

        return render(request, 'home_page/sign_up.html', {'form': user_form})
