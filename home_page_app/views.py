# Django:

from django.shortcuts import render
from .forms import *

# mysql:

from mysql.connector import connect

server_data = ['localhost', 'root', '123asd159ZXC']


def sign_in(request):

    sign_in_form = SignInForm()

    if request.method == 'POST':  # TODO доделать

        user_data = (request.POST.get('login'), request.POST.get('password'))

        conn = connect(
            host=server_data[0],
            user=server_data[1],
            password=server_data[2],
            database='account_bd_mysql'  # TODO не вышло подключиться, надо посмотреть как это сделать вообще не через
        )                                # TODO workbench

        cur = conn.cursor()

        cur.execute('SELECT EXISTS(SELECT id FROM register_data WHERE login = %s and password = %s)', user_data)

        from django.http import HttpResponse

        return HttpResponse(str(cur.fetchall()))

        return render(request, 'home_page/user_account.html', {'login': user_data[0], 'password': user_data[1]})

    else:

        return render(request, 'home_page/sign_in.html', {'form': sign_in_form})


def user_info(request):

    return render(request, 'home_page/user_info.html')
