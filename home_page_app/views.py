from django.shortcuts import render
from django.db.utils import IntegrityError
from django.http import HttpResponse

import json

from .forms import *
from .models import *

from accounts_app.models import Profile


def view_main(request):

    latest_questions = Questions.objects.order_by('-pub_date')[:5]

    match request.method:

        case 'GET':

            return render(request, 'home_page_app/index.html', {
                'latest_questions': latest_questions,
                'form': SearchQuestionForm(),
            })

        case 'POST':

            search_question_form = SearchQuestionForm(request.POST)

            if search_question_form.is_valid():

                found_questions = \
                    Questions.objects.filter(title__contains=search_question_form.cleaned_data['content'])

                if found_questions:

                    return render(request, 'home_page_app/index.html', {
                        'latest_questions': latest_questions,
                        'form': search_question_form,
                        'found_questions': found_questions,
                    })

                else:

                    return render(request, 'home_page_app/index.html', {
                        'latest_questions': latest_questions,
                        'form': search_question_form,
                    })

            else:

                return render(request, 'home_page_app/index.html', {
                    'latest_questions': latest_questions,
                    'form': SearchQuestionForm(),
                })

        case _:

            return render(request, 'error.html')


def add_question(request):

    match request.method:

        case 'POST':

            make_question_form = MakeQuestionForm(request.POST)

            if make_question_form.is_valid():

                try:

                    Questions.objects.create(
                        title=make_question_form.cleaned_data['title'],
                        content=make_question_form.cleaned_data['content'],
                        user=request.user,
                    )

                    # cash by create question:

                    user = Profile.objects.get(user_id=request.user.id)

                    user.cash += 10

                    user.save()

                    return render(request, 'home_page_app/create_question_successfully.html')

                except IntegrityError:

                    return render(request, 'home_page_app/create_question.html', {
                        'form': make_question_form,
                        'comment': 'Not unique text!',
                    })

            else:

                return render(request, 'home_page_app/create_question.html', {'form': MakeQuestionForm()})

        case 'GET':

            return render(request, 'home_page_app/create_question.html', {'form': MakeQuestionForm()})

        case _:

            return render(request, 'error.html')


def view_question(request, question_id):

    def get_comments():

        comments = Comments.objects.filter(question_id=question_id).order_by('likes').order_by('-pub_date')

        #for i in comments:
        #    if i.likes is None:
        #        i.likes = 0

        return comments

    question = Questions.objects.get(id=question_id)

    question_data = {
        'title': question.title,
        'content': question.content,
        'likes': question.total_likes(),
        'author': question.user.username,
        'pub_date': question.pub_date,
        'comments': get_comments(),
        'id': question_id,
    }

    if request.method == 'POST' and request.accepts('ajax_like'):

        user = request.user

        match request.POST.get('object_type'):

            case 'question':

                if question.likes.filter(id=user.id).exists():
                    question.likes.remove(user)

                else:
                    question.likes.add(user)

                return HttpResponse(
                    json.dumps({
                        'likes_value': question.total_likes(),
                    }),
                    content_type='application/json',
                )

            case 'comment':

                comment_id = request.POST.get('object_id')
                comment = Comments.objects.get(id=comment_id)

                if comment.likes.filter(id=user.id).exists():
                    comment.likes.remove(user)

                else:
                    comment.likes.add(user)

                return HttpResponse(
                    json.dumps({
                        'likes_value': comment.total_likes(),
                    }),
                    content_type='application/json',
                )

            case _:
                return HttpResponse(
                    json.dumps({
                        'likes_value': request.POST.get('object_id')
                    }),
                    content_type='application/json',
                )

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
                        question_id=question_id,
                        content=make_comment_form.cleaned_data['content'],
                        user=request.user,
                    )

                    # cash by create comment:

                    user = Profile.objects.get(user_id=request.user.id)

                    user.cash += 5

                    user.save()

                    question_data['comments'] = get_comments()

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
