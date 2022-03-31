from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    data = {'message': 'ko..'}

    return render(request, 'home_page/index.html', context=data)


def about(request):
    return HttpResponse('<h2>About us.</h2>')


def contact(request):
    return HttpResponse('<h2>Contact with us.</h2>')


def user_info(request, user_id, user_name):
    return HttpResponse('<h2>User name: {0}<br>Id: {1}</h2>'.format(user_name, user_id))


def error(request):
    return HttpResponse('<h1>Incorrect web-address.</h1>')
