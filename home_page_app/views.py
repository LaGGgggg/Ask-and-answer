# Django:

from django.shortcuts import render
from .forms import *

# mysql:

from mysql.connector import connect

# server data for mysql

server_data = ['localhost', 'root', '123asd159ZXC']


def sign_in(request):

    sign_in_form = SignInForm()

    if request.method == 'POST':

        user_form = SignInForm(request.POST)

        if user_form.is_valid():

            user_data = (request.POST.get('login'), request.POST.get('password'))

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

                return render(request, 'home_page/sign_in.html', {'form': sign_in_form,
                                                                  'comment': 'Wrong data, try again.'})

            else:

                # account in database, return account page

                render_data = {
                    'login': user_data[0],
                    'password': user_data[1],
                    'user_id': user_id[0],
                }

                return render(request, 'home_page/user_account.html', render_data)

        else:

            # invalid user data page

            return render(request, 'home_page/sign_in.html', {'form': sign_in_form,
                                                              'comment': 'Wrong data, try again.'})

    else:

        # standard data input page

        return render(request, 'home_page/sign_in.html', {'form': sign_in_form})


def user_info(request):

    return render(request, 'home_page/user_info.html')
