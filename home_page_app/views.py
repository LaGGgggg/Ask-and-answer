# Django:

from django.shortcuts import render
from .forms import *
from .models import *

from django.db.utils import IntegrityError

# postgresql:

from psycopg2 import connect


def view_main(request):

    latest_questions = Questions.objects.order_by('-pub_date')[:5]

    return render(request, 'home_page_app/index.html', {'latest_questions': latest_questions})


def add_question(request):

    match request.method:

        case 'POST':

            make_question_form = MakeQuestionForm(request.POST)

            match make_question_form.is_valid():

                case True:

                    try:

                        Questions.objects.create(
                            title=make_question_form.cleaned_data['title'],
                            content=make_question_form.cleaned_data['content'],
                            author_name=request.user.username,
                        )

                    except IntegrityError:

                        return render(request, 'home_page_app/create_question.html', {
                            'form': make_question_form,
                            'comment': 'Not unique text!',
                        })

                    return render(request, 'home_page_app/create_question_successfully.html')

                case False:

                    return render(request, 'home_page_app/create_question.html', {'form': MakeQuestionForm()})

        case 'GET':

            return render(request, 'home_page_app/create_question.html', {'form': MakeQuestionForm()})

        case _:

            return render(request, 'error.html')


def view_question(request, question_id):

    question = Questions.objects.get(id=question_id)

    question_data = {
        'title': question.title,
        'content': question.content,
        'likes': question.likes_value,
        'author': question.author_name,
        'pub_date': question.pub_date,
        'comments': Comments.objects.order_by('likes_value'),
    }

    match request.method:

        case 'POST':

            make_comment_form = MakeCommentForm(request.POST)

            if make_comment_form.is_valid():

                if Comments.objects.filter(content=make_comment_form.cleaned_data['content']).exists():

                    return render(request, 'home_page_app/view_question.html', {
                        'question_data': question_data,
                        'form': MakeCommentForm(),
                        'comment': 'Not unique text!',
                    })

                else:

                    Comments.objects.create(
                        question_id=question,
                        content=make_comment_form.cleaned_data['content'],
                        author_name=request.user.username,
                    )

                    question_data['comments'] = Comments.objects.order_by('likes_value')

                    return render(request, 'home_page_app/view_question.html', {
                        'question_data': question_data,
                        'form': MakeCommentForm(),
                    })

            else:

                return render(request, 'home_page_app/view_question.html', {
                    'question_data': question_data,
                    'form': MakeCommentForm(),
                })

        case 'GET':

            return render(request, 'home_page_app/view_question.html', {
                'question_data': question_data,
                'form': MakeCommentForm(),
            })

        case _:

            return render(request, 'error.html')
