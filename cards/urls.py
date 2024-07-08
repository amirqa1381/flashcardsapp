from django.urls import path
from django.views.generic import TemplateView
from .views import CardListView

urlpatterns = [
    path('', TemplateView.as_view(template_name='cards/home.html'), name='main'),
    path('card-list/', CardListView.as_view(), name='card-list')
]