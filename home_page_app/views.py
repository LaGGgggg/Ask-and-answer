# Django:

from django.shortcuts import render
from .forms import *
from .models import *

# postgresql:

from psycopg2 import connect

# server data for mysql  # TODO del

server_data = ['localhost', 'postgres', '123asd159ZXC', '5432', 'accounts_bd_pg']  # TODO del


def del_sign_in(request):

    if request.method == 'POST':

        user_form = SignInForm(request.POST)

        if user_form.is_valid():

            user_data = (user_form.cleaned_data['login'], user_form.cleaned_data['password'])

            conn = connect(
                host=server_data[0],
                user=server_data[1],
                password=server_data[2],
                port=server_data[3],
                database=server_data[4],
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


def del_sign_up(request):

    if request.method == 'POST':

        user_form = SignUpForm(request.POST)

        # check on valid and password match

        if user_form.is_valid() and user_form.cleaned_data['password'] == user_form.cleaned_data['password_confirm']:

            user_data = (user_form.cleaned_data['login'], user_form.cleaned_data['password'])

            conn = connect(
                host=server_data[0],
                user=server_data[1],
                password=server_data[2],
                port=server_data[3],
                database=server_data[4],
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


def sign_in(request):

    if request.method == 'POST':

        user_form = SignInForm(request.POST)

        if user_form.is_valid():

            try:

                # check user exists

                user = User.objects.get(
                    login=user_form.cleaned_data['login'],
                    password=user_form.cleaned_data['password']
                )

            except User.DoesNotExist:
                return render(request, 'home_page/sign_in.html', {'form': user_form,
                                                                  'comment': 'Invalid login or password.'})

            # user exists

            return render(request, 'home_page/user_account.html', {'data': user})

        else:

            # invalid user data page

            return render(request, 'home_page/sign_in.html', {'form': user_form, 'comment': 'Invalid data, try again.'})

    else:

        # standard data input page

        user_form = SignInForm()

        return render(request, 'home_page/sign_in.html', {'form': user_form})


def sign_up(request):

    if request.method == 'POST':

        user_form = SignUpForm(request.POST)

        if user_form.is_valid():

            user_data = [user_form.cleaned_data['login'], user_form.cleaned_data['password']]

            try:

                # check "login already exists"

                User.objects.get(login=user_data[0])

            except User.DoesNotExist:

                # if login not already exists, create new user

                user = User.objects.create(login=user_data[0], password=user_data[1])

                return render(request, 'home_page/user_account.html', {'data': user})

            return render(request, 'home_page/sign_up.html', {'form': user_form,
                                                              'comment': 'This login is already use, enter another please.'})

        else:

            # invalid user data page

            return render(request, 'home_page/sign_up.html', {'form': user_form, 'comment': 'Invalid data, try again.'})

    else:

        # standard data input page

        user_form = SignUpForm()

        return render(request, 'home_page/sign_up.html', {'form': user_form})
