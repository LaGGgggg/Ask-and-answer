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

            user = models.Profile.objects.get(user_id=request.user.id)

            user_cash = user.cash

            activity_dict = {'Register date: ': request.user.date_joined}

        except models.Profile.DoesNotExist:

            models.Profile.objects.create(user_id=request.user.id, cash=0)

            user_cash = 0

            activity_dict = {'Register date: ': request.user.date_joined}

        return render(request, 'accounts_app/user_profile.html', {
            'cash': user_cash,
            'activity': activity_dict,
        })
