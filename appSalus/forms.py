from django.forms import ModelForm 
from .models import Room, Dog
from django import forms

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ('name','image')

