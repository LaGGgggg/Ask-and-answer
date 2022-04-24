from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from simple_history.utils import update_change_reason

from django.shortcuts import render
from django.db.models import F
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

            # if user exist, return his money

            user_cash = user.cash

            #cash_activity = [models.Profile.history.in_bulk([user.user_id])]

            user.cash += 2

            user._change_reason = 'plus_money'  # TODO а как через явный?

            user.save(update_fields=['cash'])

            # TODO как это выбрать? cash_activity = [models.Profile.history.in_bulk(history_user_id=user.user_id)]

            #user.update(cash=F('cash') + 2)

            #update_change_reason(user, 'plus_money')

            #activity_dict = {'Register date: ': request.user.date_joined}
            activity_dict = {'Register date: ': request.user.date_joined, 'c': cash_activity}

        except models.Profile.DoesNotExist:

            # if user does not exist in table, create his with default amount of money

            models.Profile.objects.create(user_id=request.user.id)

            user_cash = 0

            activity_dict = {'Register date: ': request.user.date_joined}

        return render(request, 'accounts_app/user_profile.html', {
            'cash': user_cash,
            'activity': activity_dict,
        })
