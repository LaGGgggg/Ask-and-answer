from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.shortcuts import render
from accounts_app import models


class SignUpView(CreateView):

    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/sign_up.html'


def view_profile(request):

    if request.user.is_anonymous:

        return render(request, 'error.html')

    else:

        try:

            # check user exist

            user = models.Profile.objects.get(user_id=request.user.id)

            # if user exist, return his money and activity

            cash_activity = \
                list(models.Profile.history.filter(history_user_id=user.user_id).order_by('-history_date'))[:31]

            activity_list = []
            n = 0  # n for know previous amount of cash([12, 10,...2, 0])

            for i in cash_activity[:-1]:

                n += 1

                activity_list.append('Balance change: ' + str(cash_activity[n].cash) + ' --> ' + str(i.cash))

            user_cash = user.cash

        except models.Profile.DoesNotExist:

            # if user does not exist in table, create his with default amount of money

            models.Profile.objects.create(user_id=request.user.id)

            user_cash = 0

            activity_list = ['Here empty:(']

        return render(request, 'accounts_app/user_profile.html', {
            'cash': user_cash,
            'activity': activity_list,
        })


def add_question(request):

    if request.method == 'POST':

        return render(request, 'accounts_app/add_question_successfully.html')

    else:

        return render(request, 'accounts_app/add_question.html')
