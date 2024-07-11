from django import forms

class CardCheckForm(forms.Form):
    """
    this form is for a time that we want to know the we know the answer of the question or not 
    Args:
        forms (django form): _description_
    """
    card_id = forms.IntegerField(required=True)
    solved = forms.BooleanField(required=False)
    