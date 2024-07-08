from django.urls import path
from .views import CardListView, CreateCardView, UpdateCardView, BoxView

urlpatterns = [
    path('', CardListView.as_view(), name='card-list'),
    path("new/", CreateCardView.as_view(), name="create-card"),
    path("edit/<int:pk>/", UpdateCardView.as_view(), name="card-update"),
    path("box/<int:box_num>/", BoxView.as_view(), name='box')
]