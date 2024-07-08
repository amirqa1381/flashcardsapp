from django.shortcuts import render
from django.views.generic import ListView
from .models import Card




class CardListView(ListView):
    model = Card
    ordering = ['box', '-date_created']
    template_name = "cards/card_list.html"

