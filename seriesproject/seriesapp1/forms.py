from django import forms
from . models import seriestab

class seriesform(forms.ModelForm):
    class Meta:
        model=seriestab
        fields=['name','description','year','image']
