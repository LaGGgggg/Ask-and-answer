from django.urls import path
from django.views.generic import TemplateView

from home_page_app import views  # ignore this import error, all works correct.

urlpatterns = [
    path('', TemplateView.as_view(template_name='home_page_app/index.html')),
]
