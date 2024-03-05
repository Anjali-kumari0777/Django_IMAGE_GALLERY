from django import forms 
from .models import Imagemodel

class ImgForm(forms.ModelForm):
  class Meta:
    model=Imagemodel
    fields='__all__'
    labels={'image':''}
