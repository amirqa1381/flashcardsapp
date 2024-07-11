from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CardCheckForm
from django.views.generic import ListView, CreateView, UpdateView
from .models import Card
from django.urls import reverse_lazy
from django.http import HttpRequest
import random




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



class BoxView(CardListView):
    template_name = "cards/box.html"
    form_class = CardCheckForm
    
    def get_queryset(self):
        return Card.objects.filter(box=self.kwargs['box_num'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['box_num'] = self.kwargs['box_num']
        if self.object_list:
            context['check_card'] = random.choice(self.object_list)
        return context
    
    def post(self, request: HttpRequest, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            card = get_object_or_404(Card, id=form.cleaned_data['card_id'])
            card.move(form.cleaned_data['solved'])
        return redirect(request.META.get("HTTP_REFERER"))
    