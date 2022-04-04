from django.shortcuts import render
from django.http import HttpResponse


def user_info(request, user_name, user_id):

    data = {'user_name': user_name, 'user_id': user_id}

    return render(request, 'home_page/user_info.html', context=data)
