from django.shortcuts import render
from django.db.utils import IntegrityError
from django.http import HttpResponse

import json

from .forms import *
from .models import *

from accounts_app.models import Profile


def view_main(request):

    latest_questions = Questions.objects.order_by('-pub_date')[:5]

    if request.method == 'GET':

        return render(request, 'home_page_app/index.html', {
            'latest_questions': latest_questions,
            'form': SearchQuestionForm(),
        })

    elif request.method == 'POST':

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

    else:
        return render(request, 'error.html')


def add_question(request):

    if request.method == 'POST':

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

    elif request.method == 'GET':
        return render(request, 'home_page_app/create_question.html', {'form': MakeQuestionForm()})

    else:
        return render(request, 'error.html')


def view_question(request, question_id):

    get_comments = Comments.objects.filter(question_id=question_id).order_by('likes').order_by('-pub_date')

    question = Questions.objects.get(id=question_id)
    user = request.user
    is_liked = question.likes.filter(id=user.id).exists()

    question_data = {
        'title': question.title,
        'content': question.content,
        'likes': question.total_likes(),
        'author': question.user.username,
        'pub_date': question.pub_date,
        'comments': get_comments,
        'is_liked': is_liked,
        'id': question_id,
    }

    # Ajax request:
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == 'POST':

        if request.POST.get('object_type') == 'question':

            if question.likes.filter(id=user.id).exists():
                question.likes.remove(user)

            else:
                question.likes.add(user)

            return HttpResponse(
                json.dumps({
                    'comments_likes_values': question.total_likes(),
                }),
                content_type='application/json',
            )

        elif request.POST.get('object_type') == 'comment':

            comment_id = request.POST.get('object_id')
            comment = Comments.objects.get(id=comment_id)

            if comment.likes.filter(id=user.id).exists():
                comment.likes.remove(user)

            else:
                comment.likes.add(user)

            return HttpResponse(
                json.dumps({
                    'comments_likes_values': comment.total_likes(),
                }),
                content_type='application/json',
            )

    elif request.method == 'POST':

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

                question_data['comments'] = get_comments

                return render(request, 'home_page_app/view_question.html', {
                    'question_data': question_data,
                    'form': MakeCommentForm(),
                })

        else:

            return render(request, 'home_page_app/view_question.html', {
                'question_data': question_data,
                'form': MakeCommentForm(),
            })

    elif request.method == 'GET':

        return render(request, 'home_page_app/view_question.html', {
            'question_data': question_data,
            'form': MakeCommentForm(),
        })

    else:
        return render(request, 'error.html')
