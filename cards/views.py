from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import Card
from django.urls import reverse_lazy




class CardListView(ListView):
    model = Card
    ordering = ['box', '-date_created']
    template_name = "cards/card_list.html"



class CreateCardView(CreateView):
    """
    this class is for creating the card for the user , actually user can add card for him or her self
    and work and train 

    Args:
        CreateView (view): this is a class that we inherite form it
    """
    model = Card
    fields = ["question", "answer", "box"]
    success_url = reverse_lazy("create-card")
    template_name = "cards/card_form.html"
    
    
class UpdateCardView(CreateCardView,UpdateView):
    """
    this class is for updating the card info , and here i inherite form the createcardview because fields 
    of the createcardview and updatecardview are the same
    Args:
        UpdateView (view): this is the class that we inherite from it
    """
    success_url = reverse_lazy("card-list")
    