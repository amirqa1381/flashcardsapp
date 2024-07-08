from django.db import models


NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)

class Card(models.Model):
    """
    this class is a model for showing the card and make answer and question for it

    Args:
        models (_type_): _description_
    """
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    box = models.IntegerField(choices=zip(BOXES, BOXES), default=BOXES[0])
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.question