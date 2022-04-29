# Django:

from django.shortcuts import render
from .forms import *
from .models import *

# postgresql:

from psycopg2 import connect


def add_question(request):

    match request.method:

        case 'POST':

            make_question_form = MakeQuestionForm(request.POST)

            match make_question_form.is_valid():

                case True:

                    return render(request, 'home_page_app/create_question_successfully.html')

                case False:

                    make_question_form = MakeQuestionForm()

                    return render(request, 'home_page_app/create_question_successfully.html', {
                        'form': make_question_form,
                        'comment': 'Incorrect data, try again.'
                    })

                case _:

                    return render(request, 'error.html')

        case 'GET':

            make_question_form = MakeQuestionForm()

            return render(request, 'home_page_app/create_question.html', {'form': make_question_form})

        case _:

            return render(request, 'error.html')
