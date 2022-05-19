from django.urls import path, re_path

from home_page_app import views  # ignore this import error, all works correct.

urlpatterns = [
    re_path('^question-view/(?P<question_id>\\d+)/$', views.view_question, name='question-view'),
    path('create-question/', views.add_question, name='create-question'),
    path('', views.view_main, name='main'),
]
