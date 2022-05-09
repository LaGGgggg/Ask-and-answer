from django.urls import path
from django.views.generic import TemplateView

from accounts_app import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.view_profile, name='profile'),
    path('logout/', TemplateView.as_view(template_name='registration/logout.html'), name='logout'),
]
