from django.urls import path

from accounts_app import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.view_profile),
]
