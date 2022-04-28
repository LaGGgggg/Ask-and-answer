# Django:

from django.shortcuts import render
from .forms import *
from .models import *

# postgresql:

from psycopg2 import connect


def add_question(request):

    if request.method == 'POST':

        return render(request, 'accounts_app/add_question_successfully.html')

    else:

        return render(request, 'accounts_app/add_question.html')

