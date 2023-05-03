from django import forms
from app.models import *
class topicform(forms.ModelForm):
    class Meta:
        model=Topic 
        fields='__all__'