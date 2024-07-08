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
    
    
    def move(self, solved):
        """
        this function is for checking the user recall the answer of the question or not 
        if user recall it then we can move the card forward and if the user does not know and does not 
        recall the answer we move the card back to the first box...
        Args:
            solved (bool): this is for cheking the user recall it or not
        """
        new_box = self.box + 1 if solved else self.box - 1
        
        if new_box in BOXES:
            self.box = new_box
            self.save()
        return self
        
    
    def __str__(self) -> str:
        return self.question