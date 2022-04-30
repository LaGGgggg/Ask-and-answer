# Django:

from django.shortcuts import render
from .forms import *
from .models import *

# postgresql:

from psycopg2 import connect


def view_main(request):

    latest_questions = Questions.objects.order_by('pub_date')[:5]

    return render(request, 'home_page_app/index.html', {'latest_questions': latest_questions})


def add_question(request):

    match request.method:

        case 'POST':

            make_question_form = MakeQuestionForm(request.POST)

            match make_question_form.is_valid():

                case True:

                    Questions.objects.create(
                        title=make_question_form.cleaned_data['title'],
                        content=make_question_form.cleaned_data['content'],
                        author_name=request.user.username,
                    )

                    return render(request, 'home_page_app/create_question_successfully.html')

                case False:

                    make_question_form = MakeQuestionForm()

                    return render(request, 'home_page_app/create_question.html', {'form': make_question_form})

                case _:

                    return render(request, 'error.html')

        case 'GET':

            make_question_form = MakeQuestionForm()

            return render(request, 'home_page_app/create_question.html', {'form': make_question_form})

        case _:

            return render(request, 'error.html')


def view_question(request, question_id):

    question = Questions.objects.get(id=question_id)

    question_data = {
        'question_title': question.title,
        'question_content': question.content,
        'question_likes': question.likes_value,
        'question_author': question.author_name,
        'question_pub_date': question.pub_date,
    }

    return render(request, 'home_page_app/view_question.html', {'question_data': question_data})
