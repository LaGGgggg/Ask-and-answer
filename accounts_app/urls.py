from django.urls import path
from django.views.generic import TemplateView

from accounts_app import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view()),
    path('profile/', views.view_profile),
    path('logout/', TemplateView.as_view(template_name='registration/logout.html')),
]
