from django import forms
from .models import ToDotb

class ToDoForm(forms.ModelForm):
    class Meta:
        model=ToDotb
        fields=['task','priority','date']